Vous pouvez créer une collection simple d'éléments ordonnés en utilisant une liste Python. Par exemple :

`fruits = ["Cherry", "Apple", "Pear"]`

ou

`states_of_america = ["Delaware", "Pennsylvania", "New Jersey", "Georgia", "Connecticut", "Massachusetts", "Maryland", "South Carolina", "New Hampshire", "Virginia", "New York", "North Carolina", "Rhode Island", "Vermont", "Kentucky", "Tennessee", "Ohio", "Louisiana", "Indiana", "Mississippi", "Illinois", "Alabama", "Maine", "Missouri", "Arkansas", "Michigan", "Florida", "Texas", "Iowa", "Wisconsin", "California", "Minnesota", "Oregon", "Kansas", "West Virginia", "Nevada", "Nebraska", "Colorado", "North Dakota", "South Dakota", "Montana", "Washington", "Idaho", "Wyoming", "Utah", "Oklahoma", "New Mexico", "Arizona", "Alaska", "Hawaii"]`

### Accéder aux éléments dans les listes

Vous pouvez fournir le nom de la liste suivi de crochets et de l'indice de l'élément que vous souhaitez. Par exemple :

`states_of_america[0]`

vous donnera "Delaware".

N'oubliez pas qu'en informatique, le premier chiffre que nous utilisons pour compter est 0 et non 1. Donc 0, 1, 2, 3 au lieu de 1, 2, 3, 4.

### Indices négatifs

Vous pouvez accéder aux éléments d'une liste en comptant depuis la fin en utilisant des nombres entiers négatifs. Par exemple :
```
fruits = ["Cherry", "Apple", "Pear"]
fruits[-1] # ceci donnera "Pear"
```

### Modifier des éléments

Vous pouvez utiliser la même syntaxe pour accéder aux éléments d'une liste et les modifier. Par exemple :
```
fruits = ["Cherry", "Apple", "Pear"]
fruits[0] = "Orange"
# la liste fruits sera maintenant ["Orange", "Apple", "Pear"]
```

### Ajouter des éléments

Vous pouvez ajouter des éléments à la fin d'une liste en utilisant la fonction `append()`. Par exemple :
```
fruits = ["Cherry", "Apple", "Pear"]
fruits.append("Orange")
# la liste fruits sera maintenant ["Cherry", "Apple", "Pear", "Orange"]
```

### Documentation sur les listes

Vous pouvez trouver la documentation sur les listes Python et d'autres fonctions liées aux listes ici : https://docs.python.org/3/tutorial/datastructures.html