# Correction exercice Docker

## Exercice 0

3. `docker stop contIDorName`  
`docker ps`  
`docker pas -a`  
`docker rm contIDorName`  
`docker rm $(docker ps -aq)`  
`docker image list` = `docker images`  
`docker image rm imageID` = `docker rmi imageID`  
`docker rmi $(docker image list -a)`  

## Exercice 1

1. `docker search python` et `docker run -it python`  
2. a) `docker run --rm -v "$(pwd)":/src python ls -la`  
b) `docker run --rm -v "$(pwd)":/src python python /src/hello.py`  

## Exercice 2

Dockerfile :
```docker
FROM python

COPY hello.py /src/hello.py

CMD ["python", "/src/hello.py"]
```

`docker build -f "Dockerfile_hello_py" -t hello:script .`

## Exercice 3

1. OK  
2. Dockerfile :
```docker
FROM nginx:latest 

COPY hello.html /usr/share/nginx/html
```
  
3. `docker build -f "Dockerfile_hello_html" -t hello:html .`  
4. `docker run -d -p 8080:80 hello:html`  
5. OK
6. `docker run -d -p 8080:80 -v "$(pwd)":/usr/share/nginx/html nginx:latest`

## Exercice 4

### 1ère approche : sans docker-compose

1. `docker network create flask_net`

2. `docker volume create mdb_data`

3. `docker run -d --network flask_net --name mdb_container -v mdb_data --env MARIADB_ROOT_PASSWORD=$mariadb_pwd mariadb:latest`

Pour tester si le conteneur est bien actif et accessible : `docker exec -it mdb_container mariadb -uroot -p`

4. Dockerfile :

```docker
FROM python:3.10

ARG arg_pwd

ENV DB_HOST="mdb_container"
ENV DB_USER="root"
ENV DB_PASSWORD=$arg_pwd
ENV DB="app_db"

COPY Projet_Flask/ /src

WORKDIR /src

RUN apt-get update && apt-get install ffmpeg libsm6 libxext6  -y

RUN pip install -r requirements.txt

EXPOSE 5000
 
CMD ["python", "script_app.py"]
```

`docker build --build-arg arg_pwd=$mariadb_pwd -f Dockerfile_wo_compose -t flask_docker:wo_compose .`

5. `docker run -it --network flask_net -p 5000:5000 flask_docker:wo_compose`

Ne pas oublier les quelques modifications nécessaires dans le script_app.py notamment les variables d'environnement de BDD et le host et port dans app.run
Aussi, j'ai précisé les versions dans le requirements, notamment au niveau de sklearn pour s'assurer que les modèles sont entraînés et prédits sur des versions identiques.

### 2ème approche : avec docker-compose

6. Docker-compose.yml :

```docker
version: '3'

services:
    app:
        build: .
        depends_on:
            db:
                condition: service_healthy
        environment:
            - DB_HOST=db
            - DB_USER=root
            - DB_PASSWORD=$DB_PASSWORD
            - DB=app_db
        ports:
            - 5000:5000
        volumes:
            - ./Projet_Flask:/src           
    db:
        image: mariadb:latest
        environment:
            - MYSQL_ROOT_PASSWORD=$DB_PASSWORD
            - MYSQL_DATABASE=app_db
        volumes:
            - mariadb_data:/var/lib/mysql
        healthcheck:
            test: "mariadb $$MYSQL_DATABASE -uroot -p$$MYSQL_ROOT_PASSWORD -e 'SELECT 1;'"
            interval: 2s
            timeout: 2s
            retries: 10

volumes:
    mariadb_data:
        driver: local
```
et le Dockerfile associé pour la création de l'image de l'app

```docker
```

La variable `$DB_PASSWORD` dans le `docker-compose.yml` fait référence a un fichier `.env` enregistré dans le même dossier que le `docker-compose.yml`.

.env :
```
DB_PASSWORD="votre_mdp_préféré"
```

`docker-compose up [--build -d]`
