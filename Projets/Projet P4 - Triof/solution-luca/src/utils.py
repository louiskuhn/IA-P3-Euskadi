import requests
import os
import numpy as np
from keras.preprocessing import image
# from PIL import Image
# from skimage import transform

from azure.keyvault.secrets import SecretClient
from azure.identity import DefaultAzureCredential
from azure.cognitiveservices.vision.customvision.prediction import CustomVisionPredictionClient
from msrest.authentication import ApiKeyCredentials

VISION_PREDICTION_ENDPOINT = "https://triofmodeleclassificationdechet-prediction.cognitiveservices.azure.com/"

# vision_prediction_key = os.environ['VISION_PREDICTION_KEY'] # plus besoin de ça une fois qu'on a fait la suite avec les secrets

keyVaultName = "triof-vault"
KVUri = f"https://{keyVaultName}.vault.azure.net"
secretName = 'triof-custom-vision-prediction-key'

# Ici soit DefaultAzureCredential est vide et il utilise votre connection depuis la CLI,
# soit on précise le client_id de l'identité managée (pour quand le code sera déployé sur App Services)
# on peut aussi le préciser avec la variable d'environnement AZURE_CLIENT_ID dans App Services
credential = DefaultAzureCredential(managed_identity_client_id="b382adcf-959e-4942-a9ad-b8911ce323fa")
client = SecretClient(vault_url=KVUri, credential=credential)

vision_prediction_key = client.get_secret(secretName)



def open_waste_slot():

    """
        open the machine so that
        a user can enter the machine
    :return:
    """

    send_command_to_machine("open_waste_slot")
    return True


def close_waste_slot():
    """
    close the waste box for user safety
    :return:
    """

    send_command_to_machine("close_waste_slot")
    return True


def process_waste(waste_type):

    """
    move the good slot and shredd the waste
    :return:
    """

    move_container(waste_type)
    was_sucessful = shred_waste()

    return was_sucessful


def move_container(waste_type):

    BOTTLE_BOX = 0
    GLASS_BOX = 1
    command_name = "move_container"

    if waste_type == "bottle":
        send_command_to_machine(command_name, BOTTLE_BOX)
    elif waste_type == "glass":
        send_command_to_machine(command_name, GLASS_BOX)

    return True


def send_command_to_machine(command_name, value=None):

    """
    simulate command sending to rasberry pi
    do nothing to work even if the machine is not connected

    :param command_name:
    :param value:
    :return:
    """
    return True



def shred_waste():

    send_command_to_machine("shred_waste")

    return True



def get_custom_vision_predictions_by_api(image_content):
    headers = {
        "Prediction-Key": vision_prediction_key.value,
        "Content-type": "application/octet-stream"
    }
    r = requests.post("https://triofmodeleclassificationdechet-prediction.cognitiveservices.azure.com/customvision/v3.0/Prediction/f1c9c927-37f4-4d70-8f75-30cee8d46634/classify/iterations/Iteration1/image",
                        headers = headers,
                        data = image_content)
    
    response_body = r.json()

    predictions = response_body.get('predictions')
    print(predictions)

    return predictions

def get_custom_vision_predictions_by_sdk(image_content):


    prediction_credentials = ApiKeyCredentials(in_headers={"Prediction-key": vision_prediction_key.value})
    predictor = CustomVisionPredictionClient(VISION_PREDICTION_ENDPOINT, prediction_credentials)

    publish_iteration_name = "Iteration1"
    project_id = "f1c9c927-37f4-4d70-8f75-30cee8d46634"
    results = predictor.classify_image(
        project_id, publish_iteration_name, image_content)
    
        
    return results.predictions

# def get_prediction_is_clean_tflite(interpreter, image_path):
#     interpreter.allocate_tensors()

#     input_details = interpreter.get_input_details()
#     output_details = interpreter.get_output_details()

#     # Chargement de l'image + preprocessing
#     image = Image.open(image_path)
#     image = np.array(image).astype('float32')/255
#     image = transform.resize(image, (150, 150, 3))
#     image = np.expand_dims(image, axis=0)

#     # Prédiction
#     interpreter.set_tensor(input_details[0]['index'], image)
#     interpreter.invoke()
#     output_data = interpreter.get_tensor(output_details[0]['index'])

def get_prediction_is_clean(model, filepath):

    img_load = image.load_img(filepath, target_size=(150, 150))
    img_array = image.img_to_array(img_load)
    img_array /= 255. # remettre les valeurs de pixel entre 0 et 1
    img_array = img_array.reshape((1, 150, 150, 3)) # reshape correctement pour que le modèle accepte

    prediction = model.predict(img_array)

    final_pred = True

    decision_threshold = 0.5 # seuil de décision

    try:
        final_pred = True if prediction[0][0] < decision_threshold else False 
        print(prediction[0][0])
    except IndexError:
        print("clean/dirty model prediction didn't work")
    return final_pred