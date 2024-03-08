import os
from flask import Flask, render_template, request, flash, redirect
from werkzeug.utils import secure_filename
import tensorflow as tf

import src.utils as utils

# import tflite_runtime.interpreter as tflite
# pip install tflite-runtime NE MARCHE QUE SUR LINUX (peut-être mac à voir)


base_image_location = "camera"

UPLOAD_FOLDER = 'static/uploaded_images'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['SECRET_KEY'] = 'random secret string2'

# Chargement du modèle tflite au lancement de l'app
# interpreter = tflite.Interpreter(model_path="static/model/model_dirtyclean.tflite")

# Chargement du modèle keras au lancement de l'app
model = tf.keras.models.load_model('static/model/saved_model.keras')


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

class APIException(Exception):
    "Raised when the API Call returns no prediction"
    pass

@app.errorhandler(APIException)
def api_error(e):
    # note that we set the 500 status explicitly
    return render_template('api_error.html', exception = e), 500

@app.route('/')
def home():
    return render_template('home.html')


# En appelant Custom Vision avec l'url de son API
@app.route('/start', methods=['GET', 'POST'])
def insert():
    utils.open_waste_slot()

    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        # if user does not select file, browser also
        # submits an empty part without filename
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(filepath)
            is_clean = utils.get_prediction_is_clean(model, filepath)
            if is_clean:
                with open(filepath, "rb") as image_contents:

                    data = image_contents.read()
                    predictions = utils.get_custom_vision_predictions_by_api(data)
                    if predictions is None:
                        raise APIException
                    
                return render_template('insert.html', predictions=predictions, image_name = filename)
                    
            else:
                # return a new template saying this garbage is dirty and unrecyclable
                flash("garbage is too dirty to recycle")
                return render_template('insert.html', image_name = filename, is_clean=False)

            

    return render_template('insert.html')

# en appelant Custom Vision depuis la SDK Azure Custom Vision
@app.route('/start_sdk', methods=['GET', 'POST'])
def insert_sdk():


    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        # if user does not select file, browser also
        # submits an empty part without filename
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(filepath)

            is_clean = utils.get_prediction_is_clean(model, filepath)

            if is_clean:
                with open(filepath, "rb") as image_contents:

                    data = image_contents.read()
                    predictions = utils.get_custom_vision_predictions_by_sdk(data)
                    if predictions is None:
                        raise APIException
                    
                return render_template('insert.html', predictions=predictions, image_name = filename)
                    
            else:
                # return a new template saying this garbage is dirty and unrecyclable
                flash("garbage is too dirty to recycle")
                return render_template('insert.html', image_name = filename, is_clean=False)

    return render_template('insert.html')



@app.route('/waste/pick-type')
def pick_type():
    utils.close_waste_slot()

    return render_template('type.html')


@app.route('/confirmation', methods=['POST'])
def confirmation():
    waste_type = request.form['type']

    utils.process_waste(waste_type)
    return render_template('confirmation.html')


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
