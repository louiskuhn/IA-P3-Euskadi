# Rétropropagation

Ajustement de **tous les poids** du réseau en même temps en fonction de leur impact sur l'erreur

## L'algorithme

1. initialisation des poids (proches de 0 mais différents de 0)
2. envoi d'une observation (la première) dans le réseau
3. *feedforward* : calculer la prédiction en activant les neurones les uns à la suite des autres
4. comparaison des valeurs réelle et prédite -> fonction de coût
5. *rétropragation* : màj les poids selon leur responsabilité dans l'erreur (taux d'apprentissage = de "combien" on "met à jour" les poids)
6. répéter :
> 6.a) les opérations 2 à 5 pour **chaque observation** = apprentissage renforcé (algorithme du gradient stochastique)
> 6.b) les 2 et 3 pour plusieurs observation, puis 4 puis 5 pour tout le petit groupe d'observations = apprentissage par (mini-)lots ou *batch*
7. Quand toutes les observations sont passées une fois dans l'algo = **1 epoch**

## Sources

http://neuralnetworksanddeeplearning.com/chap2.html
