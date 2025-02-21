Les fonctions se terminent au mot-clé `return`. Si vous écrivez du code en dessous de l'instruction return, ce code ne sera pas exécuté.

Cependant, vous pouvez avoir plusieurs instructions return dans une même fonction. Alors, comment cela fonctionne-t-il?

### Retours Conditionnels

Lorsque nous avons un contrôle de flux, comme dans le code se comportera différemment (suivra différentes voies d'exécution) en fonction de certains contrôles conditionnels, nous pouvons finir avec plusieurs fins (retours).

par exemple
```
def peutAcheterDeLAlcool(age):
    if age >= 18:
        return True
    else:
        return False
```

### Retours Vides
Vous pouvez également écrire return sans rien après, et cela indique simplement à la fonction de quitter.

par exemple
```
def peutAcheterDeLAlcool(age):
    # Si le type de données de l'entrée d'âge n'est pas un entier, alors sortir.
    if type(age) != int:
        return

    if age >= 18:
        return True
    else:
        return False
```