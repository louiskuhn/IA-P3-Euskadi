from flask import Flask, render_template, request, url_for
from src.utils import *
import tflite_runtime.interpreter as tflite

app = Flask(__name__)
camera_folder = 'static/images/camera'

# Chargement de la clé API de prédiction avec CustomVision
prediction_key = os.getenv("customvision_api_key")

# Chargement du modèle au lancement de l'app
interpreter = tflite.Interpreter(model_path="./static/model/model_dirtyclean.tflite")

@app.route('/')
def home():
    return render_template('home.html')


@app.route('/start')
def insert():

    open_waste_slot()

    return render_template('insert.html')


@app.route('/waste/pick-type')
def pick_type():
    close_waste_slot()

    return render_template('type.html')

@app.route('/waste/pick-type-with-API')
def pick_type_with_API():
    close_waste_slot()

    content_type = 'application/octet-stream'
    model_url = 'https://westeurope.api.cognitive.microsoft.com/customvision/v3.0/Prediction/aa6f7947-9fff-470f-94e8-15ce914b3e52/classify/iterations/Iteration1/image'
        
    img_name, img = take_trash_picture(camera_folder)
    prediction = predict_type_with_CustomVision(os.path.join(camera_folder, img_name), prediction_key, content_type, model_url)
    
    return render_template('type.html', picture_taken=img_name, predicted_type=prediction[0], predicted_proba=round(prediction[1]*100))

@app.route('/waste/dirty-clean', methods=['GET', 'POST'])
def pick_type_with_dirty_check():
    close_waste_slot()

    content_type = 'application/octet-stream'
    model_url = 'https://westeurope.api.cognitive.microsoft.com/customvision/v3.0/Prediction/aa6f7947-9fff-470f-94e8-15ce914b3e52/classify/iterations/Iteration1/image'

    if request.method == "POST":
        img_name = request.form['img']
        prediction = predict_type_with_CustomVision(os.path.join(camera_folder, img_name), prediction_key, content_type, model_url)
        return render_template('type.html', picture_taken=img_name, predicted_type=prediction[0], predicted_proba=round(prediction[1]*100))


    # chargement de l'image
    img_name, img = take_trash_picture(camera_folder)
    img_path = os.path.join(camera_folder, img_name)

    # appeler is_clean
    clean = is_clean(interpreter,img_path)

    # si clean prédiction avec API
    if clean :
        prediction = predict_type_with_CustomVision(os.path.join(camera_folder, img_name), prediction_key, content_type, model_url)
        return render_template('type.html', picture_taken=img_name, predicted_type=prediction[0], predicted_proba=round(prediction[1]*100))
    
    # sinon vue intermédiaire pour laisser au user la possibilité de laver puis confirmer, ou confirmer direct si erreur de prédiction
    else :
        return render_template('dirty.html', picture_taken=img_name, clean=clean)

@app.route('/confirmation', methods=['POST'])
def confirmation():
    waste_type = request.form['type']

    process_waste(waste_type)
    return render_template('confirmation.html')


if __name__ == "__main__":
    app.run(debug=True)
