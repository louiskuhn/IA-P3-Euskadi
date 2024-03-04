# Amélioration grâce à l'IA d'une application existante

Ce projet est un équivalent de ce que vous pourriez faire pour votre projet E2. Il va permettre de revoir pas mal de choses notamment : 
- la gestion de projet Agile
- un peu de dev à travers du packaging d'application avec Flask et des appels à une API externe
- la reconnaissance d'image avec 2 approches (la seconde étant **facultative**) :
>- une solution Cloud
>- une solution *on-premise*, c'est-à-dire locale
- la restitution des résultats (rapport et présentation orale)

## Contexte

Triof est une start-up de tri et de recyclage des déchets spécialisée dans le traitement des déchets plastiques. Elle a développé une machine qu'elle loue aux entreprise : grâce à cette dernière les salariés peuvent déposer leurs déchets plastiques afin qu'ils soient recyclés en fil d'impression 3D.

Il est important de trier les déchêts plastiques avant de les recycler car la température de fusion de chaque plastique est différente. L'entreprise a donc conçu une interface où l'utilisateur sélectionne le type de dêchet qu'il dépose dans la machine. 

Malheureusement on a remarqué que les personnes n'indiquaient pas toujours bien quel déchet ils inséraient or cela a un impact négatif sur la qualité du filament.

Triof vous sollicite pour proposer une solution intégrant de l'IA afin de pallier ce problème. Ils vous suggèrent d'utiliser les services Cloud dans un premier temps.

## 1ère partie : questions préliminaires

### 1. Généralités sur l'intégration d'une IA dans une application existante

1. Expliquer en un paragraphe ce qu'est l'architecture client/serveur et quels sont ses avantages.
2. Expliquer ce qu'est un *web service* et son utilité dans le développement d'applications.
3. Expliquer en quoi un modèle packagé dans un *web service* permet de l'utiliser en production.

### 2. Généralités sur les solutions Cloud de Computer Vision

Dans la mesure on nous sommes ici à l'école IA **Microsoft**, et qu'on a réussi à vous avoir quelques crédits pour utiliser Azure, on utilisera dans ce projet Custom Vision de Azure Cognitive Services
1. Décrire en quelques ligne le fonctionnement, le mode de tarification et le coût de ce service.
2. Quels autres services Cloud fournis par différents providers (azure, google, amazon, ovh, etc) permettraient de répondre à la problématique exposée ?
3. Comparer ces différents services notamment en termes de coût, de mode de tarification, de rapidité. Vous pouvez synthétiser tout ça dans un tableau.

### 3. L'application Triof : analyse et compréhension du problème

Il s'agit dans un premier temps d'analyser le fonctionnement de l'application et d'expliquer votre compréhension du problème.

Pour cela, détailler les différents éléments de l'application : 
- la structure globale,
- les différents fichiers .py, .html, .css,
- que font les fonctions python
- etc...

### 4. Proposition d'une solution

Une fois cette partie terminée, vous devez avoir une vision nette du fonctionnement de l'application, une compréhension claire du problème et une idée des solutions Cloud existantes. Vous êtes donc en mesure de proposer une solution basée sur les services IA Cloud pour répondre au problème.

## 2ème partie : une solution IA Cloud

Élaboration, construction et intégration d'une solution utilisant Custom Vision de Azure Cognitive Services afin d'améliorer la classification des déchets de la machine Triof. Tout est dit ;)

### Gestion de projet Agile

Mettez en place **un planning Agile pour la construction d'une solution Cloud**.
Les 2 points fondamentaux de cette étape sont :
1. l'anticipation et la plannification des tâches (sachant que les questions préliminaires vous ont déjà fait gagner un peu de temps...)
2. l'estimation du temps passé sur chaque tâche

### Indications pour la mise en place de la solution Cloud

1. Entraîner sur Custom Vision un modèle de reconnaissance d'image permettant d'identifier les 3 types de déchets plastiques distingués par l'application (il y aura quelques étapes préalables notamment la création d'un groupe de ressources,  d'une ressource Cognitive Service et d'un projet Custom Vision)
2. Après avoir publié le modèle pour qu'il soit mobilisable par API, intégrer un appel API dans l'application en mettant en place la solution qui vous parait la plus adaptée : précocher le type de déchet plastique, suggérer le type de déchet, etc...

## 3ème partie facultative : une amélioration via une solution locale

### Re-contexte

Quelques mois se sont écoulés et Triof, très satisfait de votre travail, fait de nouveau appel à vous car ils font face à un autre problème : l'insertion par les salariés de déchets plastiques **sales** ce qui entraîne là encore, un fil d'impression de moindre qualité.

En revanche, une contrainte supplémentaire est qu'il ne veulent pas utiliser à nouveau Custom Vision afin de pouvoir monter en compétence sur l'IA en développant un modèle en local.

Proposer cette fois une solution sans recourir aux services IA Cloud pour résoudre ce problème.


### Indications pour la mise en place de la solution *on-premise*

- Vous êtes relativement libres sur cette partie mais l'idée est de construire un modèle permettant de classifier, en plus du type de déchet, la propreté du déchet.
- Vous pourrez soit construire votre propre modèle soit utiliser du *transfer learning* à partir de modèles de computer vision pré-implémentés.
- Une étape cruciale va être la constitution de votre jeu de données d'entraînement. Plusieurs solutions sont possibles notamment le scraping. Quoi qu'il en soit, n'oubliez pas l'existence de la *data augmentation*...
