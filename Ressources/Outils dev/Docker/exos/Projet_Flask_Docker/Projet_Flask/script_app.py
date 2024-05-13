from flask import Flask, url_for, render_template, request, flash, redirect
import mysql.connector as mariadb
import pandas as pd
import os
import requests
import json
from datetime import datetime

#import spécifique à la partie MNIST
os.environ["CUDA_VISIBLE_DEVICES"] = ""

import pickle
import base64
import cv2
import numpy as np
from scipy import ndimage
from keras.models import load_model
#-------------------------------------------#

#Nom de l'application
app = Flask(__name__)
app.secret_key = "a_secret_key"

#Paramètres de connexion MariaDB
mariadb_host = os.environ.get('DB_HOST')
mariadb_user = os.environ.get('DB_USER')
mariadb_pwd = os.environ.get('DB_PASSWORD')
mariadb_db = os.environ.get('DB')

#Paramètres de connexion MariaDB - OLD
#mariadb_user = os.getenv("mariadb_usr")
#mariadb_pwd = os.getenv("mariadb_pwd")

#Paramètres de recherche sur l'API de finance
url_quot = 'https://devapi.ai/api/v1/markets/quote'
url_srch = 'https://devapi.ai/api/v1/markets/search'
url_news = 'https://devapi.ai/api/v1/markets/news'
headers = {'Authorization': f'Bearer 531|hjUYrly7nmNixSdXz8tkult2MtdoKjQvc5JX5kDU'}


#Page d'accueil
@app.route("/")
def home():
    return render_template("home.html")

###################################
#######   QUESTIONS 1 à 6   #######
###################################
#Page de formulaire, envoi des données et affichage du message de bienvenu
@app.route("/test-formulaire", methods=["GET", "POST"])
def formulaire():
    if request.method == "POST":
        prenom = request.form["prenom"]
        nom = request.form["nom"]
        sex = request.form["sex"]
        user = request.form["user"]

        #Connection (et création si nécessaire) de la base de données et de la table users
        app_db = mariadb.connect(host=mariadb_host, user=mariadb_user, password=mariadb_pwd)
        curseur = app_db.cursor()
        curseur.execute("CREATE DATABASE IF NOT EXISTS app_db")
        curseur.execute("USE app_db")
        curseur.execute("CREATE TABLE IF NOT EXISTS users (prenom VARCHAR(255), nom VARCHAR(255), sex ENUM('male', 'female'), pseudo VARCHAR(255), unique(pseudo))")

        try : #on essaye d'ajouter la ligne dans la base
            curseur.execute(f"INSERT INTO users VALUES ('{prenom}', '{nom}', '{sex}', '{user}')")
            app_db.commit()
            flash("Compte crée avec succès !", "success") #si ça fonctionne, on affiche message de succès
            curseur.close()
            app_db.close() 
            return render_template("greetings.html", prenom=prenom, nom=nom, sex=sex, user=user) #on renvoie le html greetings avec la petite phrase de bienvenue

        except mariadb.Error: #comme on a mis le pseudo en unique, s'il y a 2 fois le même, il y aura une erreur mysql.connector lors de l'insertion
            app_db.rollback()
            curseur.close()
            app_db.close()
            flash("Ce pseudo est déjà pris...", "warning") #pour l'affichage d'un message d'erreur "dynamique"
            return redirect(url_for('formulaire'))
        
    return render_template("formpage.html")

#Page d'affichage des utilisateurs inscrits dans la bdd
@app.route("/utilisateurs-inscrits")
def see_users():
    try: #on essaye de se connecter à la bdd
        app_db = mariadb.connect(host=mariadb_host, user=mariadb_user, password=mariadb_pwd, database=mariadb_db)
        curseur = app_db.cursor()
        curseur.execute("SELECT * FROM users") #si ça marche, on récupère les users
        liste_users = list()
        for user in curseur:
            liste_users.append(user)#qu'on stocke dans une liste
        curseur.close()
        app_db.close()
        return render_template("userspage.html", liste_users=liste_users)#puis on renvoie le html avec tableau contenant les individus de la liste
    
    except mariadb.Error:#sinon on retourne un message d'erreur et on renvoie au formulaire
        flash("Problème de connexion à la base de données...a priori, elle n'existe pas. Il faut créer des utilisateurs !", "error")
        return redirect(url_for('formulaire'))


##################################
#######     QUESTION 7     #######
##################################
# page de récupération et affichage des donées financières via API
@app.route("/finance", methods=["GET", "POST"])
def finance_data():
    if request.method == "POST":
        search = request.form.get("search")
        ticker = request.form.get("company")

        if search:
            search = search.replace(" ", "")
            APIrequest = requests.request('GET', url_srch, headers=headers, params={'search': search})

            companies = [(comp['name'], comp['symbol']) for comp in APIrequest.json()['body']]
            return render_template("finance.html", search=search, companies=companies)

        if ticker:
            APIrequest = requests.request('GET', url_quot, headers=headers, params={'ticker': ticker})
            resp = APIrequest.json()
            quotes = resp.get('body', None)

            APIrequest = requests.request('GET', url_news, headers=headers, params={'ticker': ticker})
            resp = APIrequest.json()
            news = resp.get('body', None)
    
            try :
                #Connection (et création si nécessaire) de la base de données et de la table logs
                app_db = mariadb.connect(host=mariadb_host, user=mariadb_user, password=mariadb_pwd)
                curseur = app_db.cursor()
                curseur.execute("CREATE DATABASE IF NOT EXISTS app_db")
                curseur.execute("USE app_db")
                curseur.execute("CREATE TABLE IF NOT EXISTS logs (timestamp DATETIME, ticker VARCHAR(255), entreprise VARCHAR(255), prix VARCHAR(255), news VARCHAR(255))")
                newrow = f"INSERT INTO logs VALUES ('{datetime.now()}', '{ticker}', '{quotes['companyName']}', '{quotes['primaryData']['lastSalePrice']}', '{news[1]['title']}')"
                curseur.execute(newrow)
                app_db.commit()
                curseur.close()
                app_db.close() 
            
            except:
                flash("Données non disponibles/incomplètes pour cette entreprise ou problème d'API", "warning")
            
            return render_template("finance.html", ticker=ticker, quotes=quotes, news=news)
    
    return render_template("finance.html")

##################################
#######     QUESTION 8     #######
##################################
#Page des statistiques sur données chargées par l'utilisateur 
@app.route("/stats-csv")
def page_stats():
    return render_template("statspage.html")

#Upload des données et affichage des statistiques
@app.route("/stats-csv", methods=["POST"])
def data_stats():
    df = pd.read_csv(request.files.get("file"),request.form["sep"])
    stats_num = round(df.describe(),2)
    stats_cat = round(df.select_dtypes(include = "object").describe(),2)
    return render_template("statspage.html", data=[stats_num.to_html(), stats_cat.to_html()])


##################################
#######     QUESTION 9     #######
##################################
# ça c'est juste pour récupérer la liste des tickers dispo sur alphavantage
df = pd.read_csv("https://www.alphavantage.co/query?function=LISTING_STATUS&apikey=demo",
                 usecols=[0,1])
# et un peu de nettoyage + on en vire un peu parce qu'il y en a trop sinon
df.dropna(inplace=True)
df = df[(df.symbol.str.len()  <= 4) & (df.symbol.str.len()  <= 40)]
df.drop_duplicates(subset=['name'], inplace=True, keep='first')
companies = df.values.tolist()

# le graphique avec données financières récupérées par API
@app.route("/finance-chart", methods=["GET", "POST"])
def finance_chart():
    params = request.args

    if len(params) == 0:
        return render_template("chart.html", companies=companies)
    
    ticker = params.get("symbol")
    key = "LKHRF3ZA6N6K78WG" #"JTV6AT91QI2OSUZS"
    url = f"https://www.alphavantage.co/query?function=TIME_SERIES_MONTHLY&symbol={ticker}&apikey={key}"
    response = requests.get(url).json()

    try:
        infos = response["Meta Data"] 
        data = response["Monthly Time Series"]

        data = [{
            "time": ts,
            "open": float(data[ts]["1. open"]),
            "high": float(data[ts]["2. high"]),
            "low": float(data[ts]["3. low"]),
            "close": float(data[ts]["4. close"]),
            "volume": float(data[ts]["5. volume"])}
            for ts in data.keys()]

        return render_template("chart.html", companies=companies, infos=infos, data=data)
    
    except:
        return render_template("chart.html", companies=companies, message="Données non disponibles")

##################################
####### QUESTIONS 10 ET 11 #######
##################################
#chargement du modèle
rf = pickle.load(open('MNIST models/mnist_rf.sav', 'rb'))
cnn = load_model('MNIST models/mnist_cnn.h5')

########### Version avec fenêtre de dessin et XML
### L'utilisation du XML permet d'interagir avec le serveur et notamment de récupérer/modifier
### des données de la page sans avoir à recharger la page: ici, on s'en sert pour envoyer les
### données de l'image et mettre à jour certains éléments seulement du html, en l'occurence la
### valeur prédite (cf le script img_to_dataurl.js)

#page de dessin d'un chiffre
@app.route("/mnist")
def mnist():
    return render_template("mnist.html")

#récupération de l'image et prédiction
@app.route('/dataurl', methods=['POST'])
def predict_from_dataurl():
    #récupération des données de l'image depuis l'URL base64
    imgstring = request.form.get('data')

    #conversion en array de pixels grayscale
    encoded_data = imgstring.split(',')[1]
    arr = np.frombuffer(base64.b64decode(encoded_data), np.uint8)
    img = cv2.imdecode(arr, cv2.IMREAD_GRAYSCALE)

    #conversion array 140*140 en array 28*28 en moyennant les pixels par groupe de 5*5 
    img = img.reshape(28,5,28,5).mean(-1).mean(1)

    #récupération du centre de masse de l'image pour la décaler et la recentrer
    cy, cx = ndimage.center_of_mass(img)
    shiftx = (14-cx).astype(int)
    shifty = (14-cy).astype(int)
    M = np.float32([[1, 0, shiftx], [0, 1, shifty]]) #matrice de transformation pour une translation
    img = cv2.warpAffine(img, M, (28, 28), borderMode=cv2.BORDER_CONSTANT, borderValue=255)

    #prédiction RF
    pred = rf.predict(img.reshape(1,-1))[0]

    # prédiction CNN
    pred_probas = cnn.predict(img.reshape(1, 28, 28, 1).astype("float64") / 255,
                              verbose=0)
    pred2 = np.argmax(pred_probas)
    
    preds = {'rf': str(pred), 'cnn': str(pred2)}
    print(preds)
    return json.dumps(preds)

########### Version avec upload d'image
#page de dessin d'un chiffre
@app.route("/mnist2")
def mnist2():
    return render_template("mnist2.html")
    
#récupération de l'image et prédiction
@app.route('/mnist2', methods=['POST'])
def predict_from_img():
    uploaded_img = request.files.get("image")

    base64img = "data:image/png;base64,"+base64.b64encode(uploaded_img.getvalue()).decode('ascii')
    try :
        img = cv2.imdecode(np.frombuffer(uploaded_img.read(), np.uint8), cv2.IMREAD_GRAYSCALE)
    except cv2.error:
        flash("Soit y a un problème sur l'image uploadée, soit y a pas d'image uploadée...", "error")
        return redirect(url_for('mnist2'))


    cy, cx = ndimage.measurements.center_of_mass(img)
    shiftx = (14-cx).astype(int)
    shifty = (14-cy).astype(int)
    M = np.float32([[1, 0, shiftx], [0, 1, shifty]])
    img = cv2.warpAffine(img, M, (28, 28), borderMode=cv2.BORDER_CONSTANT, borderValue=255)

    pred = rf.predict(img.reshape(1,-1))[0]

    return render_template("mnist2.html", base64img=base64img, pred=pred)



########### Version avec fenêtre de dessin mais sans utilisation du XML
#page d'upload
@app.route("/mnist3")
def mnist3():
    return render_template("mnist3.html")
    
#récupération de l'image et prédiction
@app.route('/mnist3', methods=['POST'])
def predict_from_dataurl_wo_xml():
    #récupération des données de l'image depuis l'URL base64
    imgstring = request.form.get('data')

    #conversion en array de pixels grayscale
    encoded_data = imgstring.split(',')[1]
    arr = np.frombuffer(base64.b64decode(encoded_data), np.uint8)
    img = cv2.imdecode(arr, cv2.IMREAD_GRAYSCALE)

    #conversion array 140*140 en array 28*28 en moyennant les pixels par groupe de 5*5 
    img = img.reshape(28,5,28,5).mean(-1).mean(1)

    #récupération du centre de masse de l'image pour la décaler et la recentrer
    cy, cx = ndimage.measurements.center_of_mass(img)
    shiftx = (14-cx).astype(int)
    shifty = (14-cy).astype(int)
    M = np.float32([[1, 0, shiftx], [0, 1, shifty]]) #matrice de transformation pour une translation
    img = cv2.warpAffine(img, M, (28, 28), borderMode=cv2.BORDER_CONSTANT, borderValue=255)

    #prédiction
    pred = rf.predict(img.reshape(1,-1))[0]

    return render_template("mnist3.html", base64img=imgstring, pred=str(pred))


#on lance le serveur pour exécuter l'application
if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
