# Veille introductive au Deep Learning

La consigne est claire et simple: faire vos recherches pour répondre aux questions suivantes, si possible en comprenant ce que vous lisez/écrivez, c'est mieux.

## Les réseaux de neurones

On parle des ANN pour Artifical Neural Network qui est le terme générique pour tous les réseaux de neurones.

**Généralités**
1. Quelques premiers éléments historiques : date de création, auteurs, idée/concept ?
2. Lien avec le cerveau humain : comment fonctionne un neurone humain ? En quoi est-ce similaire ?
3. Quels sont les différents types de réseaux existants ? Quelles sont les applications ?
4. Quels sont les principaux éléments composant un ANN ?
5. Pour reprendre la question précédente mais en plus subtile : quels sont les paramètres et les hyper-paramètres d'un réseau de neurones ?
6. Quelles sont les différentes couches *(layer)* ?

**Fonction de combinaison**
1. Kézako ?
2. En quoi diffèrent les réseaux Multi-Layer Perceptron (MLP) et Radial Basis Function (RBF) ? Nous on va s'en tenir aux MLP c'est déjà bien.

**Fonction d'activation**
1. Re-kézako ?
2. Quelles sont les fonctions d'acitvation usuelles ? Ça vous rappelle rien...?

**Rétropropagation de l'erreur**
1. Re-re-kézako ?
2. Sans entrer trop dans les maths car je risque de vous perdre, essayer de comprendre et d'expliquer avec vos mots les grandes lignes et étapes de l'algorithme de rétropropagation de l'erreur.

**Un petit exemple pour voir si vous avez compris jusqu'ici**
1. Définir un réseau de neurones *(i.e un nombre d'inputs, d'outputs, de couches, de neurones dans chaque couche, une fonction de combinaison et une fonction d'activation)* pour effectuer une régression linéaire
2. Idem pour une régression logistique

## Keras
1. Décrire les étapes générales typiques pour définir, entraîner et utiliser un réseau de neurones dans Keras
2. Comment crée-t-on un modèle ? Décrire les différentes méthodes par des exemples
3. Chercher la définition des paramètres learning_rate, batch_size, epochs, metrics, optimizer, loss et illustrer avec des exemples
4. Qu'est-ce que le dropout ? Comment y fait-on appel dans un modèle ?
5. Qu'est-ce que la "batch normalization" ? Comment y fait-on appel ?
6. Chercher les cas d'applications des fonctions d'activation suivantes :
    * sigmoïde
    * tanh
    * ReLu
7. Quelles fonctions d'activation pour les problèmes de classification ?


## TensorFlow
1. Quel est le rapport entre Keras et TensorFlow ?
2. Quand utiliser TensorFlow plutôt que Keras ?

## Des ressources
- https://www.youtube.com/watch?v=XUFLq6dKQok&list=PLO_fdPEVlfKoanjvTJbIbd9V5d9Pzp8Rw
- https://playground.tensorflow.org/
- https://www.youtube.com/watch?v=aircAruvnKk
