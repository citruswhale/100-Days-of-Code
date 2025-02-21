Auparavant, nous avons vu que les fonctions nous permettent de regrouper du code dans un bloc nommé qui peut être utilisé à plusieurs reprises ultérieurement.

### PAUSE 1 - Révision
- Créez une fonction appelée `greet()`.
- Écrivez 3 instructions `print` à l'intérieur de la fonction.
- Appelez la fonction `greet()` et exécutez votre code.

### Entrées
En ajoutant un nom de variable entre parenthèses lorsque nous créons (définissons) une nouvelle fonction, cela permet à cette fonction d'accepter des entrées lorsqu'elle est appelée.

Cela signifie que nous pouvons modifier le comportement de la fonction à chaque fois en passant différentes entrées.

```
# Création de la fonction
def myFunction(input):
    print(f"Hey! {input}")
```
```
# Utilisation de la fonction
myFunction("Tommy") 
# Affiche "Hey! Tommy"
```

### Les entrées sont des variables
Lorsque vous créez une fonction avec des entrées, vous définissez un nom de variable qui sera attribué aux données qui sont transmises.

Le nom de la variable d'entrée, par exemple `name` dans ce code ici : `def greet(name):` est appelé le paramètre.

La valeur de la variable d'entrée, par exemple `Angela` quand vous appelez la fonction `greet` précédente : `greet("Angela")` est appelée l'argument.