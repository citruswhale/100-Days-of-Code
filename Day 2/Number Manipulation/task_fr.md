### Planchage d'un nombre
Vous pouvez plancher un nombre ou supprimer tous les décimales en utilisant la fonction `int()` qui convertit un nombre à virgule flottante (avec des décimales) en un entier (nombre entier).

`int(3.738492) # Devient 3`

### Arrondissement d'un nombre
Cependant, si vous voulez arrondir un nombre décimal au nombre entier le plus proche en utilisant la méthode mathématique traditionnelle, où tout ce qui est supérieur à .5 est arrondi à la hausse et tout ce qui est inférieur est arrondi à la baisse. Alors vous pouvez utiliser la fonction `round()` de python.

`round(3.738492) # Devient 4`

`round(3.14159) # Devient 3`

`round(3.14159, 2) # Devient 3.14`

### Opérateurs d'affectation
Les opérateurs d'affectation tels que l'opérateur d'affectation d'addition `+=` ajoutera le nombre à droite à la valeur originale de la variable à gauche et attribuera la nouvelle valeur à la variable.

`+=`

`-=`

`*=`

`/=`


### f-Strings
En Python, nous pouvons utiliser les f-strings pour insérer une variable ou une expression dans une chaîne de caractères.

`age = 12`

`print(f"J'ai {age} ans")`

`# Affichera J'ai 12 ans.`