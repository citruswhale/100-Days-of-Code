### Longueur d'une liste  
Vous pouvez obtenir la longueur d'une liste (nombre d'éléments dans la liste) ou la longueur d'une chaîne (nombre de caractères dans la chaîne) en utilisant la fonction `len()`. https://docs.python.org/3/library/functions.html#len  

### IndexError  
Lorsque vous essayez d'accéder à un élément qui n'est pas dans l'intervalle de la liste, vous obtiendrez une erreur IndexError. Par exemple :  

```
fruits = ["Cherry", "Apple", "Pear"]
print(fruits[3]) #Cela entraînera une erreur IndexError
```

### Listes imbriquées  
Vous pouvez intégrer des listes dans d'autres listes, ce que l'on appelle une "Liste imbriquée" ou une "Liste 2D". Par exemple :  

```
fruits = ["Cherry", "Apple", "Pear"]
veg = ["Cucumber", "Kale", "Spinnach"]
fruits_and_veg = [fruits, veg]
#La liste ressemblerait à ceci : [["Cherry", "Apple", "Pear"], ["Cucumber", "Kale", "Spinnach"]]
```
Vous pourriez également représenter la liste au format 2D comme ceci :  
```
["Cherry", "Apple", "Pear"]
["Cucumber", "Kale", "Spinnach"]
```