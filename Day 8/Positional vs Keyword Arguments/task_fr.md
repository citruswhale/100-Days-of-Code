### Entrées multiples
Vous pouvez avoir plusieurs entrées dans les fonctions. Tout ce que vous devez faire est de les séparer par une virgule `,`.

### PAUSE 1
Créez une fonction avec plusieurs entrées

<div class="hint">
  <code>
def saluer(nom, salutation):
  
    ____print(f"{salutation} {nom}")
    
saluer("Angela", "Yo!")
</code>
</div>

### PAUSE 2
Modifiez la fonction pour qu'elle affiche les valeurs attendues.
```
def saluer_avec(nom, lieu)
    Bonjour nom
    Comment est-ce à lieu
```

### Arguments Positionnels
Par défaut, lorsque vous créez une fonction en Python, elle conservera l'ordre des arguments dans la définition de la fonction.

ex. Dans la fonction ci-dessous, le premier argument qui est entré sera toujours imprimé avant le second. `a = 2, b = 1`

```
def ma_fonction(a, b)
  print(a)
  print(b)
  
 ma_fonction(2, 1)
 #Il imprimera :
 # 2
 # 1
```

### Arguments nommés
Vous pouvez utiliser des mots-clés lorsque vous fournissez les arguments lorsque vous appelez une fonction afin qu'il y ait moins de confusion sur quelle valeur est attribuée à quel paramètre d'entrée.

### PAUSE 3 
Appelez la fonction `saluer_avec()` en utilisant des arguments nommés.

<div class="hint">
  <code>
saluer_avec(lieu="Londres", nom="Angela")
</code>
</div>