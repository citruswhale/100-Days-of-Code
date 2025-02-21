Un dictionnaire en Python fonctionne de manière similaire à un dictionnaire dans la vie réelle. C'est une structure de données qui nous permet d'associer une clé à une valeur et de coupler les deux morceaux de données ensemble.

Voici comment vous créez un dictionnaire en Python:
```
# Un exemple de dictionnaire
couleurs = {
    "pomme": "rouge", 
    "poire": "vert", 
    "banane": "jaune"
}
```

Voici comment vous récupérez des éléments à partir d'un dictionnaire :
```
print(couleurs["poire"])
# Imprimera "vert"
```

Voici comment créer un dictionnaire vide :
```
mon_dictionnaire_vide = {}
```

Voici comment vous pouvez ajouter de nouveaux éléments à un dictionnaire existant :

```
couleurs["pêche"] = "rose"
```

C'est aussi de cette manière que vous pouvez modifier une valeur existante dans un dictionnaire :
```
couleurs["pomme"] = "vert"
```

Voici comment boucler à travers un dictionnaire et imprimer toutes les clés :
```
for cle in couleurs:
    print(cle)
```

Voici comment boucler à travers un dictionnaire et imprimer toutes les valeurs :
```
for cle in couleurs:
    print(couleurs[cle])
```