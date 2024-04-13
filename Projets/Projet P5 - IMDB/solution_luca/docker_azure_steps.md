# Etapes pour déployer une appli web conteneurisé sur Azure

## 1. Préparer l'appli
- Mettre toute son appli dans un même dossier
- S'assurer que l'appli a un point d'entrée .py, idéalement app.py par convention
- Créer le requirements.txt avec les bons modules (attention pour Flask il faut parfois préciser le module Werkzeug)


## 2. Créer l'image Docker
- Se placer dans le dossier de l'appli et y créer un fichier `Dockerfile` comme dans l'exemple
- `docker build -t <nom de votre image> .`

## 3. Push son image sur un registry en ligne (ici [Azure Container Registry](https://learn.microsoft.com/en-us/azure/container-registry/container-registry-get-started-docker-cli?tabs=azure-cli))
- [Créer un Container Registry](https://portal.azure.com/#view/HubsExtension/BrowseResource/resourceType/Microsoft.ContainerRegistry%2Fregistries) (Basic Plan et privé)
- Dans un terminal ou Azure CLI est installé : `az acr login -n <nom de votre registry>`
- Créer un [tag](https://docs.docker.com/reference/cli/docker/image/tag/) qui refère à votre image :

`docker tag <tag actuel de votre image> <nom de votre registry>.azurecr.io/<nom du repository dans votre registry>`

(en général nom du repository correspond au nom du projet)

- `docker push <nom de votre registry>.azurecr.io/<nom du repository dans votre registry>`

- Vérifiez que votre image est bien dans votre registry Azure

## 4. Donner vie à son image en créant un container à partir de l'image

- Créez le container depuis votre terminal ou le Cloud Shell :
```
  az container create --resource-group <nom de votre groupe de ressources> \
    --name <nom à donner à votre container Azure> \
    --image <chemin vers votre image à récupérer sur ACR> \
    --ports <le port utilisé par votre serveur web> \
    --dns-name-label <nom UNIQUE qui va servir d'URL à votre application> --location <la région Azure>
```
- Exemple :
```
az container create --resource-group imdb_luca \
 --name imdb_prediction_container \
 --image imdbregistryluca.azurecr.io/imdb_prediction:latest \
 --ports 8080 \
 --dns-name-label imdb-luca-uniquename --location westeurope
```

- Si un username et un mot de passe vous sont demandés, rendez vous sur votre container registry et dans l'onglet Acess keys et cliquer sur Admin user pour accéder aux identifiants nécessaires.

- Il ne reste plus qu'à tester en envoyant la bonne requête à l'adresse URL qu vous avez choisi !
