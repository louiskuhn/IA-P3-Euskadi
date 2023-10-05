"""Codage des algorithmes en Python"""

# 1. Écrire un algorithme qui affiche tous les numéros de 1 à 9
for i in range(1,10):
    print(i)
    
# 2. Écrire un algorithme qui échange la valeur de deux variables
# Exemple, si a= 2 et b= 5, le programme donnera a= 5 et b= 2
def swap(a,b):
    a,b = b,a
    return a,b

x,y = 12,3
x,y = swap(x,y)
print(x,y)

# 3. Écrire un algorithme qui affiche l’alphabet à l’envers
# v1
abc = "abcdefghijklmnopqrstuvwxyz"
for lettre in abc[::-1]:
    print(lettre)

# v2
abc = "abcdefghijklmnopqrstuvwxyz"
for lettre in reversed(abc):
    print(lettre)
    
# v3
abc = "abcdefghijklmnopqrstuvwxyz"
for i in range(len(abc)):
    print(abc[len(abc)-1-i])

# v4
import string
abc = list(string.ascii_lowercase)
abc.sort(reverse=True)
print(abc)
abc.reverse()
print(abc)

# 4. Écrire un algorithme permettant d’épeler un mot en affichant chaque lettre
# successivement.
def epeler(mot):
    for l in mot:
        print(l)
epeler("salut")

# 5. Écrire un algorithme qui affiche les différentes lettres nécessaires pour 
# écrire un mot en précisant le nombre d’occurrence de la lettre dans le mot
phrase = "On s'amuse comme des FOUS avec les Dictionnaires"
# v1
def nb_lettres(ph):
    ph = ph.lower()
    dic = {}
    for l in ph :
        if l in string.ascii_lowercase:
            if l in dic : #dic.keys()
                dic[l] += 1
            else:
                dic[l] = 1
    return dic

nb_lettres(phrase)

# v2
def nb_lettres(ph):
    ph = ph.lower()
    dic = {}
    for l in ph :
        if l in string.ascii_lowercase:
            if l in dic : #dic.keys()
                pass
            else:
                dic[l] = phrase.count(l)
    return dic

nb_lettres(phrase)

# v3
from collections import defaultdict
def nb_lettres(ph):
    ph = ph.lower()
    dic = defaultdict(int)
    for l in ph :
        if l in string.ascii_lowercase:
            dic[l] += 1
    return dic

nb_lettres(phrase)

# v4
def nb_lettres(ph):
    ph = ph.lower()
    dic = {}
    for l in ph :
        if l in string.ascii_lowercase:
            dic[l] = dic.get(l, 0) + 1
    return dic

nb_lettres(phrase)

# 6. Écrire un algorithme qui demande un nombre compris entre 10 et 20, jusqu'à
# ce que la réponse convienne. En cas de réponse supérieure à 20, on fera 
# apparaître un message : “Plus petit !”, et inversement, “Plus grand !” si le
# nombre est inférieur à 10.
def nombre(inf=10, sup=20):
    nb = input("Entre un nombre : ")
    if not nb.isdigit() :
        nb = input("Entre un NOMBRE ! ")
    
    nb = eval(nb) #int
    if nb > sup :
        print("Plus petit")
        nombre(inf=inf, sup=sup)
    elif nb < inf :
        print("Plus grand")
        nombre(inf=inf, sup=sup)
    else:
        print("bravo")

nombre()
    
# 7. Écrire un algorithme qui calcule et affiche la surface d’un triangle
# connaissant sa base et sa hauteur.
def triangle(b, h):
    return b*h/2
triangle(12,6)

# 8. Écrire un algorithme qui, étant donné le prix unitaire d’un produit (hors
# TVA), le taux de TVA (en %) et la quantité de produit vendue à un client,
# calcule et affiche le prix total à payer par ce client.
def total(prix_ht, tva, quantite):
    return prix_ht*(1+tva/100)*quantite
total(0.9, 20, 10)

# 9. Écrire un algorithme qui, étant donné les résultats (note entière sur 20)
# de trois examens passés par un étudiant (exprimés par six nombres, à savoir,
# la note et la pondération de chaque examen), calcule et affiche la moyenne
# globale exprimée en pourcentage.
# v1
def moy_pond(notes, coefs):
    if len(notes) != len(coefs):
        return "erreur"
    
    som = 0
    som_c = 0
    for i in range(len(notes)):
        som += notes[i] * coefs[i]
        som_c += coefs[i]
    
    return som/som_c * 5

moy_pond([12,16,19], [3,2,5])

# v2
def moy_pond(notes, coefs):
    if len(notes) != len(coefs):
        return "les 2 listes n'ont pas la même longueur"

    return sum([n*c for n,c in zip(notes, coefs)]) / sum(coefs) * 5

moy_pond([12,16,19], [3,2,5])

#10. Écrire un algorithme qui affiche toutes les combinaisons de deux nombre
# entre 0 et 99, dans l’ordre croissant au format
# “00 01, 00 02, 00 03 … 00 99, 01 02, … 97 99, 98 99”.
# Ne pas oublier les espaces et virgules !
s = ""
for d1 in range(10):
    for u1 in range(10):
        for d2 in range(10):
            for u2 in range(10):
                if d1*10+u1 < d2*10+u2 :
                    s += f"{d1}{u1} {d2}{u2} ,"
                    #s += str(d1)+str(u1)+" "+str(d2)+str(u2)+","
s = s[:-1]
print(s)

#11. Écrire un algorithme qui calcule la somme des chiffres d’un nombre entier
# de 3 chiffres. Réflexion : l’algorithme est-il aussi valide pour les entiers
# inférieurs à 100 ?
# v1
def sum_digits(nb):
    l = [int(d) for d in str(nb)]
    return sum(l)

sum_digits(123456)

# v2 sans conversio en string
def som_digits(nb):
    c = nb//100
    d = (nb-100*c)//10
    u = nb -100*c -10*d
    return c+d+u

som_digits(123)

# v3 sans conversion et en généralisant
def som_digits(nb):
    n = 0
    while 10**n < nb :
        n += 1
    
    som = 0
    for k in range(n-1,-1,-1):
        chiffre = nb//10**k
        som += chiffre
        nb -= chiffre * 10**k
    
    return som

som_digits(123456)

#12. Écrire un algorithme itératif et un algorithme récursif qui affiche la
# somme de 1 à n
def som_i(n):
    som = 0
    for i in range(1, n+1):
        som += i
    return som

def som_r(n):
    if n == 0 :
        return 0
    else:
        return n + som_r(n-1)

som_i(43), som_r(43)

#13. Écrire un algorithme itératif et un algorithme récursif qui affiche le
# produit de 1 à n (ce qu’on appelle la factorielle n et noté n!)
def fac_i(n):
    fac = 1
    for i in range(1, n+1):
        fac *= i
    return fac

def fac_r(n):
    if n==0 :
        return 1
    else:
        return n * fac_r(n-1)

fac_i(9), fac_r(9)

#14. Écrire un algorithme itératif et un algorithme récursif qui affiche le
# n-ème terme de la suite de Fibonacci
def fibo_i(n):
    a,b = 0,1
    for i in range(n):
         a,b = b,a+b
    return a

def fibo_r(n):
    if n < 2:
        return n
    else:
        return fibo_r(n-1) + fibo_r(n-2)
    
fibo_i(10), fibo_r(10)