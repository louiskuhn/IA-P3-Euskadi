# Introduction aux tests

## Les tests

Pourquoi les tests ? Parce que si le programme fonctionne pas, ben ça marche pas. Ok mais quand on code on fait des tests au fur et à mesure pour vérifier que ça fait pas n'importe quoi donc pourquoi les tests ? Parce que les développeurs aiment automatiser tout ce qui peut l'être. Et accessoirement car quand on teste un programme au fil de l'eau, on s'assure pas nécessairement que les différentes briques fonctionneront entre elles.

L'idée c'est donc de créer un script spécifique à notre projet qui a pour seul but d'exécuter les tests automatisés (par opposition aux tests manuels exécutés "à la main").

Le principal intérêt, en dehors d'un éventuel gain de temps, c'est de voir tout de suite si un ajout des fonctionnalités risque de "casser" l'existant. Ça facilite donc le développement et surtout la collaboration.

On distingue différents types de tests. En voici quelques uns (cette liste est loin d'être exhaustive, il manque notamment les tests manuels):
- **Les tests unitaires :** vérifient qu'une fonction fait bien ce qu'elle doit faire
- **Les tests d'intégration :** vérifient que les fonctionnalités de l'application s'intègrent bien entre elles. Dans un gros projet, il y a de nombreuses fonctionnalités qui peuvent être codées par différentes personnes. Il faut donc s'assurer que toutça est bien huilé...
- **Tests fonctionnels :** vérifient qu'une fonctionnalité marche bien comme attendu. Ils correspondent à un parcours utilisateur sont généralement associés à une User Story.
- **Tests de non régression :** vérifient que la mise en place d'une nouvelle fonctionnalité n'impactera pas les fonctions déjà existantes. Les tests fonctionnels auront bien validé que la nouvelle fonction est opérationnelle mais c'est le test de non régression qui validera que cette dernière n'impacte pas les autres fonctionnalités du logiciel.

On va pour nous s'en tenir aux tests unitaires principalement.

## Doctest

Python intègre une fonctionnalité basée sur les `docstrings` pour effectuer des tests de manière simple.

Les Doctests sont des `docstrings` écrites comme un terminal python avec les `>>>` qui précèdent et le résultat attendu sans chevrons :

```python
"""
>>> from math import sqrt
>>> res = sqrt(9)
>>> res
3.0
"""
```

Puis pour exécuter, il faut lancer dans le terminal la commande `python -m doctest /path/to/your/script.py`.

Essayer par vous mêmes avec différentes fonctions de votre choix.

Bon après, c'est sympa, mais y a mieux.

## Pytest

Pytest est un framework de test en python.

Avantages:
- open-source
- tests multiples en parallèle donc rapide
- syntaxe simple
- autodétection des tests dans un projet/script
- possibilité de sauter des tests d'une suite de test

### Installation

Créer un environnement (ou pas c'est vous qui voyez !) et lancer `pip install pytest` ou `conda install pytest`.

Pour vérifier que l'installation est correcte, lancer `pytest -h` dans un terminal.

### La syntaxe et les noms

Sans nom de fichier spécifié, Pytest va exécuter tous les fichiers **test_*.py** or __*_test.py__ dans le dossier courant et les sous-dossiers

Dans un script de tests, les fonctions de test doivent :

- avoir un nom commençant par **"test"**
- contenir le mot clé `assert` suivi d'une condition à tester

Ainsi pour tester une fonction `ma_fonction` présente dans un script `mon_script.py`, il faut créer un fichier `test_mon_script.py` qui contient :

```python
from mon_script import ma_fonction

def test_ma_fonction():
    assert ma_fonction(parametres_de_ma_fonction) == resultat_attendu
```

puis lancer `pytest` depuis le terminal.


**Remarque :** si une fonction commence par "test" mais qu'on ne veut pas qu'elle constitue un test, c'est possible de le spécifier via l'attribut booléen `__test__` (soit directement, soit via un décorateur). Par exemple, le code ci-dessous ne doit exécuter **qu'un seul test**.

> ```python
> def pas_un_test(fonction):
>     fonction.__test__ = False
>     return fonction
> 
> def test_qui_en_est_pas_un_1():
>     assert False
> test_qui_en_est_pas_1.__test__ = False
> 
> @pas_un_test
> def test_qui_en_est_pas_un_2():
>     assert False
> 
> 
> def test_qui_en_est_bien_un():
>     assert True
> ```

### Un premier script de tests

1. Créer un dossier où vous voulez, qui s'appelle comme vous voulez et placer vous dedans. On y restera pour toute la suite.
2. Créer un fichier `calculette.py` avec une fonction `carre` qui retourne le carré d'un nombre
3. Créer un ficher de test `test_calculette.py` qui :

>- importe les fonctions du script `calculette.py`
>- teste la fonction `carre` dans une fonction `test_carre`

4. Lancer dans le terminal les commandes `pytest` et `pytest -v`. Quelle différence ?
5. Ajouter dans `test_calculette.py` un second test `test_carre_2` sur la fonction `carre` qui ne passera pas et réexécuter `pytest` depuis votre terminal.
6. Ajouter dans `calculette.py` une nouvelle fonction `racine` qui retourne la racine carré d'un nombre et la tester dans `test_calculette.py`.

### Plusieurs scripts de tests

En pratique, on aura généralement plusieurs scripts de tests différents. On va voir comment Pytest les gère.

7. Ajouter dans `calculette.py` une fonction `compare` qui compare 2 nombres et renvoie une chaine de caractère `"a plus grand que b"` (ou inversement).
8. Créer un nouveau fichier `test_compare.py` qui teste la fonction `compare`
9. Lancer `pytest -v`. Que se passe-t-il ? Comment lancer un fichier de test spécifique ?

### Sous-ensemble de tests

Bon, on a plein de scripts de tests, qui contiennent plein de tests pour valider tous nos modules, fonctions et fonctionnalités mais maintenant on pourrait vouloir n'exécuter qu'une partie...Pytest permet de le faire de 2 manières :

- soit en utilisant les noms des fonctions de tests
- soit en utilisant des marqueurs pour identifier les tests à effectuer

#### En utilisant les noms

10. Trouver et exécuter les commandes pour effectuer :

>- uniquement les tests contenant "carre"
>- tous les tests ne contenant pas "compare"
>- tous les tests contenant "compare" ou "racine"

#### En utilisant les marqueurs

Pour ajouter et appliquer un marqueur aux tests, cela se fait de la manière suivante :

```python
from mon_script import ma_fonction
import pytest

@pytest.mark.mon_marqueur
def test_ma_fonction():
    assert ma_fonction(parametres_de_ma_fonction) == resultat_attendu
```

11. Ajouter un marqueur "square" aux 2 tests de la fonction `carre` et un marqueur "other" aux 2 autres tests
12. Lancer séparément les tests pour :

>- le groupe de test "square"
>- tous sauf le groupe "other"
>- les groupes "square" ou "other"

### D'autres marqueurs utiles

#### Ignorer certains tests

Le marqueur `@pytest.mark.skip` permet de ne pas exécuter le test.

13. Ignorer un test avec ce marqueur

#### Tests de plusieurs paramètres

En utilisant le marqueur `@pytest.mark.parametrize`, on peut faire un test sur plusieurs jeux de paramètres.

14. Test la fonction carré sur plusieurs inputs en utilisant `@pytest.mark.parametrize`.


## Pour creuser

On peut aller beaucoup (beaucoup) plus loin que cette légère introduction et je vous conseille le cours https://openclassrooms.com/fr/courses/7155841-testez-votre-projet-python qui est assez complet, avec un exemple "fil rouge", sans être trop long ni trop compliqué.

Quelques pistes à débroussailler si vous préférez explorer par vous-même :

- Les plugins pour utiliser pytest avec flask, au hasard `pytest-flask`...
- La POO avec les tests (organisation des tests en classe)
- Le contexte des tests avec les concepts de *mocks* et de *fixtures*
- La couverture de test (ou *coverage*)
- *Test-Driven-Development*
