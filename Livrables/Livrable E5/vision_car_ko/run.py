import os
from flask import Flask, request, render_template, jsonify
from PIL import Image
import numpy as np
import json

from keras.models import load_model

import base64
from io import BytesIO

app = Flask(__name__)

@app.route('/')
def index():

    return render_template('home.html')

@app.route('/upload', methods=['GET', 'POST'])
def upload_image():

    model = load_model("unet_vgg16_categorical_crossentropy_raw_data.keras", compile=False)


    colors = np.array([[ 68,   1,  84],
    [ 70,  49, 126],
    [ 54,  91, 140],
    [ 39, 126, 142],
    [ 31, 161, 135],
    [ 73, 193, 109],
    [159, 217,  56],
    [253, 231,  36]])
    

    if request.method == 'POST':

        image = request.files['file']

    if image.filename == '':
        return "Nom de fichier invalide"

        img = Image.open(image)

        IMAGE_SIZE = 512

        img_resized = img.resize((IMAGE_SIZE, IMAGE_SIZE), resample=Image.Resampling.NEAREST)
        img_resized = np.array(img_resized)

        img_resized = np.expand_dims(img_resized, 0)
        img_resized = img_resized / 255.

        predict_mask = model.predict(img_resized, verbose=0)
        predict_mask = np.argmax(predict_mask, axis=3)
        predict_mask = np.squeeze(predict_mask, axis=0)
        predict_mask = predict_mask.astype(np.uint8)
        predict_mask = Image.fromarray(predict_mask)
        predict_mask = predict_mask.resize((img.size[0], img.size[1]), resample=Image.Resampling.NEAREST)
        
        predict_mask = np.array(predict_mask)
        predict_mask = colors[predict_mask]
        predict_mask = predict_mask.astype(np.uint8)

        buffered_img = BytesIO()
        img.save(buffered_img, format="PNG")
        base64_img = base64.b64encode(buffered_img.getvalue()).decode("utf-8")

        buffered_mask = BytesIO()
        base64_mask = base64.b64encode(buffered_mask.getvalue()).decode("utf-8")

        print("Finished")

        return json({'message':"predict ok", "img_data":base64_img, "mask_data":base64_mask})
    


if __name__ == '__main__':
    app.run(debug=True, port=8000)