Une fonction, dans sa forme la plus simple, n'est qu'un nom qui encapsule un bloc de code. Vous lui donnez un nom, et lorsque vous appelez la fonction par ce nom, tout le code contenu dans le bloc de la fonction sera exécuté. Cela peut nous aider à gagner du temps et à réduire le code répétitif.

### Définir une nouvelle fonction
```
def <nom de la fonction>():
    print("Bonjour")
    # Faire autre chose
    # Faire autre chose ...
```

### Appeler une fonction
Appeler une fonction signifie simplement déclencher l'exécution de celle-ci. Nous pouvons appeler une fonction à tout moment dans notre code en Python.

```
<nom de la fonction>()
```

Mettons tout ensemble, par exemple :
```
#Création de la fonction
def obtenir_nom_utilisateur():
    nom = input("Quel est votre nom ? ")
    print("Bonjour, " + nom)
    # À l'intérieur de la fonction

#En dehors de la fonction
print("Bonjour")
obtenir_nom_utilisateur() # Appeler la fonction
```

Ce code produira la séquence de sortie suivante :
```
Bonjour
Quel est votre nom ? #Je tape Angela
Bonjour
Angela