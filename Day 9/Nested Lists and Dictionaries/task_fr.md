Vous pouvez combiner différents types de données pour obtenir la structure souhaitée.

### Imbriquer une liste dans un dictionnaire
Au lieu d'assigner une valeur de type Chaîne à une clé, nous pouvons la remplacer par une Liste. Vous pouvez imbriquer une Liste dans un Dictionnaire de cette manière :

```
my_dictionary = {
    key1: [Liste],
    key2: Valeur,
}
```

### PAUSE 1
Voyez si vous pouvez comprendre comment imprimer "Lille" à partir de la liste imbriquée appelée `travel_log`.
```
travel_log = {
    "France": ["Paris", "Lille", "Dijon"],
    "Germany": ["Stuttgart", "Berlin"],
}
```
<div class="hint">
  Pour obtenir cette partie : <code>["Paris", "Lille", "Dijon"]</code>
Vous auriez besoin : <code>travel_log["France"]</code>

Donc, pour obtenir Lille, vous avez besoin :
<code>travel_log["France"][1]</code>
</div>

### Imbriquer des listes à l'intérieur d'autres listes

Nous avons déjà vu des listes imbriquées :

```
nested_list = ["A", "B", ["C", "D"]]
```

### PAUSE 2
Vous souvenez-vous comment obtenir des éléments qui sont profondément imbriqués dans une liste ? Essayez d'imprimer "D" à partir de la liste `nested_list`.

<div class="hint">
  Pour obtenir cette liste : ["C", "D"] nous avons besoin du code :

<code>nested_list[2]</code>

Donc, pour obtenir "D", nous avons besoin de :

<code>nested_list[2][1]</code>
</div>


### Imbriquer un dictionnaire dans un dictionnaire
Vous pouvez également imbriquer un dictionnaire dans un dictionnaire :

```
my_dictionary = {
    key1: Valeur,
    key2: {Cle: Valeur, Cle: Valeur},
}
```

### PAUSE 3
Essayez de comprendre comment imprimer "Stuttgart" à partir de la liste suivante :
```
travel_log = {
  "France": {
    "cities_visited": ["Paris", "Lille", "Dijon"], 
    "total_visits": 12
   },
  "Germany": {
    "cities_visited": ["Berlin", "Hamburg", "Stuttgart"], 
    "total_visits": 5
   },
}
```