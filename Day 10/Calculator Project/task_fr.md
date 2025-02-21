L'objectif est de construire un programme de calculatrice.

### Démonstration
https://appbrewery.github.io/python-day10-demo/


### Stocker des Fonctions en tant que Valeurs de Variable
Vous pouvez stocker une référence à une fonction comme valeur pour une variable.
Par exemple,
```
def ajouter(n1, n2):
    return n1 + n2
    
    
my_favourite_calculation = ajouter
my_favourite_calculation(3, 5)  # Renvoie 8
```
Dans le fichier de départ, vous verrez un dictionnaire qui référence chacun des calculs mathématiques qui peuvent être effectués par notre calculatrice. Essayez-le et voyez si vous pouvez le faire effectuer des additions, des soustractions, des multiplications et des divisions.

### PAUSE 1 
À FAIRE : Écrivez les 3 autres fonctions - soustraire, multiplier, diviser.

### PAUSE 2
À FAIRE : Ajoutez ces 4 fonctions dans un dictionnaire en tant que valeurs. Clés = "`+`", "`-`", "`*`", "`/`"

### PAUSE 3
À FAIRE: Utilisez les opérations du dictionnaire pour effectuer les calculs. Multipliez 4 * 8 en utilisant le dictionnaire.


### Fonctionnalité
- Le programme demande à l'utilisateur de taper le premier nombre.
- Le programme demande à l'utilisateur de taper un opérateur mathématique (un choix de "`+`", "`-`", "`*`" ou "`/`")
- Le programme demande à l'utilisateur de taper le deuxième nombre.
- Le programme calcule le résultat en fonction de l'opérateur mathématique choisi.
- Le programme demande si l'utilisateur veut continuer à travailler avec le résultat précédent.
- Si oui, le programme boucle pour utiliser le résultat précédent comme premier nombre puis répète le processus de calcul.
- Si non, le programme demande à l'utilisateur d'entrer à nouveau le premier nombre et efface toute mémoire des calculs précédents.
- Ajoutez le logo de art.py

<div class="hint">
  Essayez d'écrire un organigramme pour planifier votre programme.
</div>

<div class="hint">
    Pour appeler la multiplication à partir du dictionnaire des opérations, vous écririez votre code comme ceci :

<code>résultat = operations["*"](n1= 5, n2= 3)</code>

Le résultat serait alors égal à 15.
</div>