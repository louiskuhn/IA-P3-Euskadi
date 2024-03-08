import os
import random
from matplotlib.image import imread
import requests
import json
from PIL import Image
from skimage import transform
import numpy as np

def open_waste_slot():
    """
        open the machine so that
        an user can enter the machine

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


def take_trash_picture(camera_folder):
    """
        Function simulating the picture taking
        inside the machine. 

        Call this function to ask the machine to 
        take picture of the trash

        return : path to image and np array of the picture
    """

    send_command_to_machine("take_picture")

    paths = os.listdir(camera_folder)
    img_name = random.choice(paths)

    return img_name, imread(os.path.join(camera_folder, img_name))

def predict_type_with_CustomVision(img_path, prediction_key, content_type, model_url):

    headers = {'content-type':content_type, 'Prediction-Key':prediction_key}

    r = requests.post(model_url, data=open(img_path,"rb"), headers=headers)
    json_predictions = json.loads(r.content)['predictions']

    return json_predictions[0]['tagName'], json_predictions[0]['probability']

def is_clean(interpreter, imagepath):
    """
        Function predicting whether trash is clean or not
        with tflite model stored in static/model

        return : True or False
    """
    # Chargement du modèle
    interpreter.allocate_tensors()

    input_details = interpreter.get_input_details()
    output_details = interpreter.get_output_details()

    # Chargement de l'image + preprocessing
    image = Image.open(imagepath)
    image = np.array(image).astype('float32')/255
    image = transform.resize(image, (150, 150, 3))
    image = np.expand_dims(image, axis=0)

    # Prédiction
    interpreter.set_tensor(input_details[0]['index'], image)
    interpreter.invoke()
    output_data = interpreter.get_tensor(output_details[0]['index'])

    if output_data[0][0] < 0.5:
        return True
    else:
        return False