# Introduction à Flask

Maintenant que vous avez bien manipulé le notebook Intro_Flask et que Flask n'a plus de secrets pour vous, c'est parti pour la suite.
Les questions 1, 2 et 3 reprennent exactement ce qui est fait dans le notebook donc faites l'effort de le refaire par vous-même et pas seulement copier/coller une solution.
La question 4 consiste à modifier et adapter ce qui est fait dans la fin du notebook.
Enfin, à partir de la question 5, y a de la nouveauté.

### Les bases
1. Faire avec Flask une page internet sur laquelle est écrit "Hello World!"

2. Faire avec Flask une page internet sur laquelle est écrit "Hello World!" en modifiant le style (pour cela il faut donc passer par une page html et fichier css pour le style)

3. Faire avec Flask un site web contenant 2 pages (une page d'accueil et une seconde page) avec bien sûr la possibilité de passer de l'une à l'autre.

### Formulaire

4. Faire avec Flask une page /test-formulaire qui contient un formulaire permettant de rentrer le prénom, le nom, le sexe de l'utilisateur ainsi qu'un pseudo. Une fois les informations renseignées, une nouvelle page doit afficher :
"Bonjour Mr {prénom} {nom}, votre nom d'utilisateur est {pseudo}" si c'est un homme et "Bonjour Mme..." sinon.

### Base de données

5. Créer une base de données SQL contenant une table users avec comme colonnes : prenom, nom, sexe, pseudo.
Modifier /test-formulaire pour que désormais à chaque fois qu'un utilisateur rentre ses informations, celles-ci soient ajoutées dans la base de donnée. Pour cela il faudra utiliser un client sql python pour se connecter à la base de donnée.
Il faudra par ailleurs gérer le cas d’un pseudo déjà existant...

6. Faire une page /utilisateurs-inscrits qui permet de lister tous les noms d'utilisateurs présents dans la base de donnée.

7. Récupérer les news d'investissement et de bourse les plus récentes concernant une entreprise que l'utilisateur aura rentré, et les afficher. Au même moment, inscire en base de données les logs de cette recherche (user, datetime, ticker, company, price_at_datetime...) Indice : https://devapi.ai/docs#stocks-options-crypto-GETapi-v1-markets-news mais vous êtes libres d'utiliser ce que vous voulez.

### Data Science

8. Faire une page avec Flask qui affiche les statistiques de base d'un csv ou excel (gérer les deux) que l'utilisateur aurait chargé grâce à un formulaire. Vous pouvez reprendre un des nombreux datasets qu'on a utilisé lors des précédentes semaines.

9. Créer une page permettant d'afficher un graphique du prix du stock d'une entreprise dans le temps. Libre à vous d'utiliser les données récoltées grâce à la question 7 ou d'aller chercher autre part.

10. Charger un modèle entrainé sur MNIST (dessins de chiffres à classer) et afficher la prédiction du modèle lorsque l'utilisateur charge une image via un formulaire.

### Pour aller plus loin (un peu de JS n'a jamais tué personne)

11. Reprendre le projet précédent et permettre à l'utilisateur de dessiner un chiffre que le modèle pourra deviner.
