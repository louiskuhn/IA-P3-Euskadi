import pickle
from sklearn.ensemble import RandomForestClassifier 
from keras.datasets import mnist

#les données
(X_train, y_train), (X_test, y_test) = mnist.load_data()

#reshape des images sous forme d'un vecteur
X_train = X_train.reshape(60000,-1)
X_test = X_test.reshape(10000,-1)

#une forêt aléatoire
model = RandomForestClassifier(n_estimators=500, max_features=50, n_jobs=-1, verbose=True)
model.fit(X_train, y_train)

#sauvegarde du modèle
pickle.dump(model, open('MNIST models/mnist_rf.sav', 'wb'))