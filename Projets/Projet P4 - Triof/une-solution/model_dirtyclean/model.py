import os
import tensorflow as tf
from tensorflow.keras import layers, Model, Input
from tensorflow.keras.optimizers import RMSprop
from tensorflow.keras.applications import Xception
from tensorflow.keras.preprocessing.image import ImageDataGenerator
import matplotlib.pyplot as plt

# Transfert learning avec Xception comme modèle de base
xception = Xception(input_shape=(150, 150, 3),
                    include_top=False,
                    weights='imagenet')

xception.trainable = False

# Couches de sortie et nouveau modèle
inputs = Input(shape=(150, 150, 3))
x = xception(inputs, training=False)
x = layers.Flatten()(x)
x = layers.Dense(1024, activation='relu')(x)
x = layers.Dropout(0.2)(x)
outputs = layers.Dense(1, activation='sigmoid')(x)
model = Model(inputs, outputs)

# Compilation du modèle
model.compile(
    loss='binary_crossentropy',
    optimizer=RMSprop(learning_rate=0.0001),
    metrics=['acc'])

# Préparation des data et data augmentation
train_dir = 'model_dirtyclean/images/train'
val_dir = 'model_dirtyclean/images/validation'

train_clean_dir = os.path.join(train_dir, 'clean')
train_dirty_dir = os.path.join(train_dir, 'dirty')

val_clean_dir = os.path.join(val_dir, 'clean')
val_dirty_dir = os.path.join(val_dir, 'dirty')

# Data augmentation
train_datagen = ImageDataGenerator(
    rescale=1./255,
    rotation_range=40,
    width_shift_range=0.2,
    height_shift_range=0.2,
    shear_range=0.2,
    zoom_range=0.2,
    horizontal_flip=True)

val_datagen = ImageDataGenerator(rescale=1./255)

train_generator = train_datagen.flow_from_directory(
    train_dir, 
    target_size=(150, 150),  
    batch_size=20,
    class_mode='binary')

validation_generator = val_datagen.flow_from_directory(
    val_dir,
    target_size=(150, 150),
    batch_size=20,
    class_mode='binary')

print("Entrainement des dernières couches")
model.fit(
    train_generator,
    steps_per_epoch=1,
    epochs=12,
    validation_data=validation_generator,
    validation_steps=1)

# Affinage en réentrainant le TOUT le modèle avec un learning rate très faible
xception.trainable = True
model.compile(
    loss='binary_crossentropy',
    optimizer=RMSprop(learning_rate=1e-5),
    metrics=['acc'])
print("Ré-entrainement de tout le modèle")
model.fit(
    train_generator,
    steps_per_epoch=1,
    epochs=5,
    validation_data=validation_generator,
    validation_steps=1)

# Enregistrement du modèle
model.save('model_dirtyclean/saved_model')

# Export Tensorflow lite
# intéressant pour obtenir un modèle plus léger et donc plus facilement "embarquable"
converter = tf.lite.TFLiteConverter.from_saved_model('model_dirtyclean/saved_model')
tflite_model = converter.convert()
with open('static/model/model_dirtyclean.tflite', 'wb') as f:
    f.write(tflite_model)