# Faire une application web de Computer Vision avec Flask, Custom Vision & App Services

## Flask et Custom Vision
- Construire un squelette d'application Flask qui va servir votre modèle
- Créer un projet custom vision et l'entrainer: [lien](https://learn.microsoft.com/en-us/azure/ai-services/Custom-Vision-Service/getting-started-build-a-classifier)
- Utiliser le package requests pour appeler l'url de l'API de prédiction créée précédemment : [lien](https://learn.microsoft.com/en-us/azure/ai-services/Custom-Vision-Service/use-prediction-api)
- Au lieu d'utiliser l'url de l'API, télécharger le module python azure-cognitiveservices-vision-customvision pour appeler Custom Vision depuis votre code (on appele ça utiliser le Software Development Kit ou SDK) : [lien](https://learn.microsoft.com/en-us/azure/ai-services/custom-vision-service/quickstarts/image-classification)

## Azure Key Vault et les secrets
- Maintenant, au lieu de stocker la clé de l'API en clair dans le code, il est recommandé de la cacher, soit dans une variable d'environnement, soit encore mieux : dans un **Secret**. Pour cela on utilise Azure Key Vault. Voici comment créer un Key Vault et un secret dans ce coffre de clés depuis le portail Azure : [lien](https://learn.microsoft.com/en-us/azure/key-vault/secrets/quick-create-portal)
- Le but étant de mettre la valeur de cette clé d'API dans le secret. On récupère ensuite le secret depuis le code : [lien](https://learn.microsoft.com/en-us/azure/key-vault/secrets/quick-create-python?tabs=azure-cli) ***attention: Pour cela il faut installer la [CLI Azure](https://learn.microsoft.com/en-us/cli/azure/install-azure-cli)***. Une fois la CLI installée, vous pourrez lancer des commandes telles que az login depuis votre terminal.

## Déploiement, Configuration & Monitoring
- Une fois cela fait, on a une application fonctionnelle et sécurisée ! On peut maintenant la déployer sur [Azure App Services](https://discord.com/channels/1192791080362573844/1192791080362573849/1214874629844246528): [lien](https://learn.microsoft.com/en-us/azure/app-service/configure-language-python). Cela demande de créer sa webapp App Services [ici](https://portal.azure.com/#create/Microsoft.WebSite) (attention ne pas prendre un plan trop coûteux, prenez Free ou Basic B1).

*Pour faire plus simple pour l'instant, commentez la partie du code ou vous utilisez la SDK Azure Key Vault et utilisez simplement une variable d'environnement pour récupérer le secret contenant votre clé d'API. Pour ajouter une variable d'environnement à votre webapp, c'est [ici](https://learn.microsoft.com/en-us/azure/app-service/configure-common).*

- Pour la déployer, faites un .zip de tous les fichers et dossiers à la racine de votre appli, avec un requirements.txt contenant les modules nécessaires, et déployez le à l'aide de la commande : 

`az webapp deploy --name <le nom de votre app> --resource-group <le nom de votre groupe de ressouces> --src-path <le chemin vers votre .zip>`

- Attention vous aurez peut-être à définir l'abonnement par défaut pour votre compte avec la CLI. Pour vérifier le bon déroulement du déploiement de votre app, allez dans l'onglet 'Journal' ou 'Log Stream' de votre webapp.


- Pour que votre application se lance véritablement, il vous faudra ajouter un 'startup script' (onglet Settings>Configuration>General Settings). C'est un script qui se lancera à chaque démarrage de votre webapp. Ce script dépend de votre application mais typiquement il serait `python app.py`.

- Redémarrez votre webapp et testez là !

<br>

- Bonus : Pour ne plus avoir à mettre la clé d'API en variable d'environnement et que App Services puisse communiquer avec Azure Key Vault, il faut qu'il puisse s'identifier, à l'aide d'une [identité managée que vous aurez à lui créer](https://learn.microsoft.com/en-us/azure/app-service/overview-managed-identity), et il faut qu'il ait [les bons accès à Key Vault](https://learn.microsoft.com/en-us/azure/app-service/app-service-key-vault-references?tabs=azure-cli). 