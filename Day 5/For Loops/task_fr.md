Les boucles nous permettent de dire à l'ordinateur de répéter des actions sans avoir à écrire du code répétitif. Si nous voulions que l'ordinateur affiche les nombres de 1 à 100, il serait très fastidieux de taper une instruction `print` pour chaque nombre, ou même de simplement écrire tous les nombres de 1 à 100. Les boucles nous permettent de créer une règle que l'ordinateur peut suivre pour exécuter une action répétée.

### Syntaxe

```
for <nom de variable de chaque élément> in <une liste>:
    <faire quelque chose>
    <faire autre chose> 
```

### PAUSE 1 - Soyez un ordinateur
Prédisez ce qui sera affiché par le code ci-dessous :

```
fruits = ["Apple", "Peach", "Pear"]
for fruit in fruits:
    print(fruit)
    print(fruit + " pie")
```

### Indentation
L'indentation est très importante en programmation Python. Chaque fois que vous voyez le symbole `:` utilisé, vous devez faire attention à l'indentation qui suit.

Exemple : Ce code se comportera de manière très différente

```
fruits = ["Apple", "Peach", "Pear"]
for fruit in fruits:
    print(fruit)
    print("Hello")
```

de ce code :

```
fruits = ["Apple", "Peach", "Pear"]
for fruit in fruits:
    print(fruit)
print("Hello")