Le programme demandera :
```
Combien de lettres souhaitez-vous dans votre mot de passe ?
Combien de symboles souhaitez-vous ?
Combien de chiffres souhaitez-vous ?
```
L'objectif est de prendre les entrées de l'utilisateur à ces questions, puis de générer un mot de passe aléatoire. Utilisez vos connaissances sur les listes et les boucles en Python pour relever le défi.

### Démonstration
https://appbrewery.github.io/python-day5-demo/

### Version Facile
Génerez le mot de passe en séquence. Les lettres, puis les symboles, puis les chiffres. Si l'utilisateur veut 

4  lettres,
2 symboles et
3 chiffres,
alors le mot de passe pourrait ressembler à cela :

`fgdx$*924`

Vous pouvez voir que toutes les lettres sont regroupées. Tous les symboles sont regroupés et tous les chiffres se suivent également. Essayez de résoudre ce problème en premier.

<div class="hint">
  N'oubliez pas que vous pouvez utiliser la fonction random.choice() pour obtenir un élément aléatoire d'une Liste ! Mais vous devez d'abord importer le module aléatoire.
</div>


### Version Difficile
Une fois que vous avez terminé la version facile, vous êtes prêt à vous attaquer à la version difficile. Dans la version avancée de ce projet, le mot de passe final ne suit pas un schéma. Ainsi, l'exemple ci-dessus pourrait ressembler à ceci :

`x$d24g*f9`

Et chaque fois que vous générez un mot de passe, les positions des symboles, des chiffres et des lettres sont différentes. Cela rendra le mot de passe plus difficile à pirater pour les hackers.

La compétence essentielle d'un bon programmeur est d'utiliser Google pour trouver ce dont vous avez besoin. Votre cerveau est fait pour réfléchir, pas pour mémoriser les fonctions ! Vous devrez faire des recherches sur Google pour résoudre ce projet à un niveau difficile. Si vous êtes bloqué, vérifiez l'indice ci-dessous pour savoir quoi chercher sur Google.

<div class="hint">
  Essayez de chercher sur Google : "Comment mélanger des éléments dans une liste en Python"
</div>