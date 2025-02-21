### Générateurs de nombres pseudo-aléatoires
Les ordinateurs ne sont pas aléatoires, car ils sont construits avec des circuits et des commutateurs. Mais l'aléatoire est très important lors de la création de logiciels, notamment pour les jeux. Ce serait vraiment ennuyeux si chaque mouvement dans un jeu vidéo était prédéterminé.

C'est pourquoi certains informaticiens ont inventé les générateurs de nombres pseudo-aléatoires, par exemple : https://fr.wikipedia.org/wiki/Mersenne_Twister

Si vous souhaitez en apprendre davantage sur les générateurs de nombres pseudo-aléatoires, je vous recommande de regarder cette vidéo de Khan Academy : https://www.youtube.com/watch?v=GtOt7EBNEwQ&ab_channel=KhanAcademyLabs

### Le module random en Python
Consultez la documentation ici :
https://docs.python.org/3/library/random.html

Pour l'utiliser, vous devez d'abord l'importer :

`import random`

### Nombres entiers aléatoires dans une plage

```
import random
rand_num = random.randint(1, 10)

#Cela produira un nombre entier aléatoire entre 1 et 10 (inclus).
```
### Modules en Python
Python nous permet de mettre du code dans différents fichiers et d'importer ce code si nécessaire. Cela signifie que nous pouvons mieux organiser et modulariser notre code. 

Vous pouvez créer un nouveau module simplement en créant un nouveau fichier `.py`, puis vous pouvez importer des variables ou des fonctions de ce fichier en utilisant simplement le mot-clé `import`.

### Nombres flottants aléatoires
Vous pouvez générer un nombre aléatoire entre 0.0 (inclus) et 1.0 (exclu) en utilisant le code suivant du module random :

```
import random
rand_num_0_to_1 = random.random()
```
Cela peut également être représenté ainsi :

`0.0 <= random.random() < 1.0`

Vous pouvez étendre la plage des nombres aléatoires générés par cette méthode en utilisant une multiplication.

Par exemple : `random.random() * 5`

Cela générera un nombre aléatoire entre 0 et 5.

Une autre méthode pour générer des nombres à virgule flottante aléatoires est d'utiliser la fonction `uniform()`.

```
import random
random_float = random.uniform(1, 10)
#Cela générera un nombre à virgule flottante aléatoire entre 1 et 10. 
```
Cette méthode peut ou non inclure la borne supérieure selon l'arrondi du nombre à virgule flottante.
Ainsi, elle est mieux représentée comme suit :

`a <= random.uniform(a,b) <= b`

Selon que vous souhaitez inclure la borne supérieure ou non, vous choisirez d'utiliser `random.random()` ou `random.uniform()`.

### PAUSE 1 - Pile ou Face
Créez un programme de lancer de pièce utilisant ce que vous avez appris sur la randomisation en Python. Il doit afficher aléatoirement "Pile" ou "Face" à chaque exécution.

<div class="hint">
  Vous devrez réfléchir à ce que vous avez appris sur les instructions conditionnelles en Python.
</div>