""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
""""""""""""""""""""""""""""""" EXERCICES PYTHON """""""""""""""""""""""""""""
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

##### Exercice 1 : les impairs
# on choisit de pas les inclure en cas de bornes impaires
from math import ceil, floor

def impairs(a,b):
    #res = ""
    for i in range(floor(a)+1, ceil(b)):
        if i % 2 == 1 :
            print(i, end=" ")
            #res += f"{i} "
    #print(res)

impairs(11, 19.5)

##### Exercice 2 : le jeu du plus ou moins
# La solution minimale
import random
nb_a_trouver = random.randint(1,100)
nb = -1
while nb != nb_a_trouver:
    nb = eval(input("Entrer un nombre entre 1 et 100 : "))
    if nb > nb_a_trouver:
        print("Trop grand")
    elif nb < nb_a_trouver:
        print("Trop petit")
    else:
        print("Bravo")
        
# Une solution plus complète
def input_num(string):
    n =  input(string)
    try :
        return eval(n)
    except:
        print("C'est pas un nombre")
        return input_num(string)

def joueurs_scores():
    nb_joueurs = input_num("Combien êtes-vous ? ")
    scores = {}
    if nb_joueurs > 2 :
        print(f"Dommage, c'est 2 max donc y en a {nb_joueurs -2} qui vont regarder")
    
    for i in range(min(nb_joueurs, 2)):
        nom = input(f"Entrer un nom pour le joueur {i+1} : ")
        scores[nom] = 0
    
    return scores
        
def deviner(joueur, diff):
    tentative = input_num(f"{joueur}, entrer un nombre : ")
    while tentative > diff or tentative < 1 :
        print(f"Non ça doit être un nombre entre 1 et {diff}")
        return deviner(joueur, diff)
    return tentative
    
def plus_ou_moins():
    # définition du nombre de joueurs, leurs noms et leurs scores
    scores = joueurs_scores()
    joueurs = list(scores.keys())
    
    # définition un niveau de difficulté
    diff = 20*input_num("Choisir un niveau de difficulté entre 1 (très facile) et 10 (très difficile)")
    
    # premier joueur 
    num_joueur = 0
    while True:
        # faire jouer chaque joueur l'un après l'autre
        joueur_actuel = joueurs[num_joueur]
        print(f"\n\nC'est à {joueur_actuel} de deviner")
        nb_a_trouver = random.randint(1,diff)
        tentative = deviner(joueur_actuel, diff)
        cpt = 1
        while tentative != nb_a_trouver:
            print("Trop grand" if tentative > nb_a_trouver else "Trop petit")
            tentative = deviner(joueur_actuel, diff)
            cpt += 1
        print(f"Bravo, t'as trouvé en {cpt} coups")
        scores[joueur_actuel] += cpt
        if num_joueur == len(joueurs)-1:
            continuer = input("Voulez-vous continuer ? (o/n)")
            if continuer == "n":
                break
        num_joueur = (num_joueur + 1) % 2
    
    # scores finaux
    try:
        vainqueur = int(scores[joueurs[0]] > scores[joueurs[1]])
        print(f"Victoire de {joueurs[vainqueur]} : {scores[joueurs[vainqueur]]} à {scores[joueurs[(vainqueur+1)%2]]}")
    except:
        print(f"Ton score final est de {score[joueurs[0]]}")
        

##### Exercice 3 : les plus grands nombres
import random
def genere(n=100,a=0,b=10000):
    return [random.randint(a,b) for i in range(n)]

def les_plus_grands(liste, nb=10):
    best = []
    tmp = liste.copy()
    for i in range(nb):
        maxi = max(tmp)
        best.append(maxi)
        tmp.remove(maxi)
    return best

a = genere(20)
print(les_plus_grands(a,5))
print(a)

##### Exercice 4 : les algos de tri
import random
l = [random.randint(0,100) for i in range(50)]

# algo 1 : en utilisant min (tri par sélection)
def tri_min(liste):
    tri=[]
    tmp = liste.copy()
    for i in range(len(liste)):
        mini = min(tmp)
        tri.append(mini)
        tmp.remove(mini)
    return tri

# algo 2 : tri à bulles
def tri_bulles(liste):
    for i in range(len(liste)):
        mini = i
        for j in range(i+1, len(liste)):
            if liste[j] < liste[mini]:
                mini=j
        liste[i], liste[mini] = liste[mini], liste[i]
    return liste

# algo 3 : tri insertion
def tri_ins(liste):
    for i in range(1, len(liste)):
        tmp = liste[i]
        j = i
        while j>0 and tmp < liste[j-1]:
            liste[j] = liste[j-1]
            j-=1
        liste[j] = tmp
    return liste

# algo 4 : tri rapide ou tri quicksort tri par partitionnement
def tri_rapide(liste):
    if len(liste) <2 :
        return liste
    else :
        ind_pivot = random.randint(0,len(liste)-1)
        pivot = liste[ind_pivot]
        lg = []
        ld = []
        l = liste[0:ind_pivot]+liste[ind_pivot+1:len(liste)]
        for val in l:
            if val < pivot:
                lg.append(val)
            else:
                ld.append(val)
        return tri_rapide(lg) + [pivot] + tri_rapide(ld)

# comparaison des temps d'exécution
import time

sort_function = lambda l : l.sort()

durees = {}
fonctions = ["tri_min", "tri_bulles", "tri_ins", "tri_rapide", "sort_function", "sorted"]
for i in range(len(fonctions)):
    l = [random.randint(0,10000) for i in range(10000)]
    tri = eval(fonctions[i])
    debut = time.time()
    tri(l)
    durees[fonctions[i]] = time.time() - debut

durees

##### Exercice 5 : des conversions
def conv_time(s):
    reste = s
    annee = int(reste // (60*60*24*365.25))
    reste = reste % (60*60*24*365.25)
    mois = int(reste // (60*60*24*30.4375))
    reste = reste % (60*60*24*30.4375)
    jour = int(reste // (60*60*24))
    reste = reste % (60*60*24)
    heure = int(reste // (60*60))
    reste = reste % (60*60)
    minute = int(reste // 60)
    seconde = int(reste % 60)
    
    #annee = format(annee, ",").replace(",", " ")
    
    print(
        f"{s} secondes correspondent à :",
        f"{annee:,} années {mois} mois {jour} jours".replace(",", " "),
        f"{heure} heures {minute} minutes {seconde} secondes",
        sep="\n")
    
conv_time(3430061596791935255)
    
    
def conv_speed(speed):
    kmh = round(1.609 * speed, 2)
    ms = round(1609/3600 * speed, 2)
    print(f"{speed} miles/h est équivalent à :",
          f" {kmh} km/h et {ms} m/s", sep = "\n")

import random    
conv_speed(random.randint(0,300))


##### Exercice 6 : le triangle de Pascal
def pascal(i,k):
    """Fonction qui retourne le coefficient du triangle de Pascal
    à la i-ème ligne et k-ème colonne
    
    i : int, indice de ligne
    k: int, indice de colonne
    
    returns : int, coef de Pascal
    """
    if k == 1 or k == i+1:
        return 1
    else :
        return pascal(i-1, k-1) + pascal(i-1, k)
    
le_plus_grand = lambda ligne : pascal(ligne, ligne//2+1)
for i in range(1,10):
    print(le_plus_grand(i))
    
    
##### Exercice 7 : dictionnaires
def inverse(dico):
    #return {dico[cle]:cle for cle in dico}
    return {val:cle for cle,val in dico.items()}

dico = {"Bonjour":"Egun on", "Merci":"Milesker", "Bien":"Ongi"}
inverse(dico)


##### Exercice 8 : manipulation de fichiers textes
# un éditeur de texte
os.chdir("/home/elka/IA-P3-Euskadi/Projets/Projet P1 - Exercices base Python/")

def ecrire(nom):
    with open("fichiers_exos/"+nom,'a') as f:
        while True:
            ligne = input("Entre une ligne de texte ou ligne vide pour quitter : ")
            if ligne == "":
                break
            else:
                f.write(ligne + "\n")

def lire(nom):
    with open("fichiers_exos/"+nom,'r') as f:
        content = f.read()
        print(content)

def editeur():
    nom = input("Nom du fichier à éditer : ")
    choix = input('Entrer "e" pour écrire et "l" pour lire le fichier : ')
    if choix == "e":
        ecrire(nom)
    elif choix == "l":
        lire(nom)
    else:
        print("choix non cohérent")
        
                  
# les tables de multiplication
def table_multi(n):
    table = ""
    for i in range(1,21):
        table += str(i*n) + " "
    return table[:-1]

fichier = open("fichiers_exos/tables_multi.txt",'w')

for i in range(2,31):
    fichier.write(table_multi(i) + "\n")
fichier.close()
        

# les triples espaces
fichier = open("fichiers_exos/tables_multi.txt",'r+')
lignes = fichier.readlines()
for i in range(len(lignes)):
    lignes[i] = lignes[i].replace(" ", "   ")

fichier.seek(0)
fichier.writelines(lignes)
fichier.close()

# une combinaise de 2 fichiers
fileA = open("fichiers_exos/tables_multi.txt",'r')
fileB = open("fichiers_exos/file1.txt",'r')
fileC = open("fichiers_exos/combi.txt",'w')

while True:
    ligneA = fileA.readline()
    ligneB = fileB.readline()
    if ligneA == "" and ligneB == "":
        break
    if ligneA != "":
        fileC.write(ligneA)
    if ligneB != "":
        fileC.write(ligneB)

fileA.close()
fileB.close()
fileC.close()


##### Exercice 9 : les notes
import pickle
import os

# pour être au niveau du dossier contenant ce script python : 
os.chdir("/home/elka/IA-P3-Euskadi/Projets/Projet P1 - Exercices base Python/")

def save(liste, nom):
    filepath = "fichiers_exos/notes/" + nom
    with open(filepath, "wb") as f:
        pickle.dump(liste,f)

def create_or_load(nom):
    filepath = "fichiers_exos/notes/" + nom
    if os.path.exists(filepath):
        with open(filepath, "rb") as f:
            liste = pickle.load(f)
    else:
        liste = []
    return liste

def ajout_notes(liste):
    while True:
        new_note = input("Entrer un nouvelle note (pour sortir <Enter> : ")
        if new_note == "":
            break
        else:
            liste.append(eval(new_note))
            print(f'{len(liste)} notes entre {min(liste)} et {max(liste)}',
                  f'avec une moyenne de {sum(liste)/len(liste)}',
                  sep="\n")
            
def main():
    # récupération d'un nom de liste (existant ou nom)
    print("Bienvenu dans l'assistant de saisie des notes")
    action = input("Taper O pour ouvrir ou C pour créer une liste")
    if action.lower().strip() == "o":
        listes_existantes = os.listdir("fichiers_exos/notes")
        if len(listes_existantes) == 0:
            nom = input("Il y a pas de liste, entrer un nom pour une nouvelle liste : ")
            nom = nom.strip()
        else :
            print("les listes existantes sont ", listes_existantes, sep="\n")
            nom = input("Quelle liste voulez-vous ?")
            nom = nom.strip()
        
    elif action.lower().strip() == "c":
        nom = input("Entrer un nom pour votre nouvelle liste : ")
        nom = nom.strip()
    # on charge ou crée la liste  
    liste = create_or_load(nom)
    # on ajoute des notes dans la liste
    ajout_notes(liste)
    # on sauvegarde la liste
    save(liste, nom)
    print("Liste sauvegardée, au revoir")
        
    
##### Exercice 10 : une base de données
def remplir(dico):
    while True:
        nom = input("Entre le nom ou <Enter> pour terminer")
        if nom == "":
            break
        
        age = int(input("Age (entier en années) : "))
        sex = input("Sexe (M/F) : ").strip().upper()
        taille = float(input("Taille (en m) : "))
        dico[nom] = (age, sex, taille)
        
def afficher(dico):
    while True:
        nom = input("Entre le nom ou <Enter> pour terminer")
        if nom == "":
            break
        
        if nom in dico:
            age, sex, taille = dico[nom]
            print(f"{nom} : {age} ans, sexe {sex}, {taille}m")
        else:
            print("Nom inconnu")
        
def voir(dico):
    print(dico)

def enregistrer(dico):
    nom_fichier = input("Entrer un nom pour votre dictionnaire : ")
    f = open("fichiers_exos/bdd/" + nom_fichier, 'w')
    for nom, infos in dico.items():
        f.write(f"{nom}:{infos[0]},{infos[1]},{infos[2]}\n")
    f.close()
    
def charger(dico):
    nom_fichier = input("Entrer un nom de dictionnaire existant : ")
    try:
        f = open("fichiers_exos/bdd/" + nom_fichier, 'r')
        
        for l in f.readlines():
            obs = l.split(":")
            nom = obs[0]
            age, sex, taille = obs[1].split(",")
            dico[nom] = (int(age), sex.upper(), float(taille))
        
        f.close()
    except:
        print("Fichier inexistant")
    
def sortir(dico):
    print("Au revoir")
    return True
    
def main():
    dico = {}
    action = {"C":charger, "R":remplir, "A":afficher,
              "V":voir, "E":enregistrer, "S":sortir}
    while True:
        choix = input("Que souhaitez-vous faire ?\n" +\
                      "(C)harger un dictionnaire\n" +\
                      "(R)emplir un dictionnaire\n" +\
                      "(A)fficher les éléments du dictionnaire\n" +\
                      "(V)oir le dictionnaire\n" +\
                      "(E)nregegistrer un dictionnaire\n" +\
                      "(S)ortir").strip().upper()
        if action.get(choix)(dico):
            break