Vous allez construire un programme de chiffrement et de déchiffrement en utilisant le [chiffre César](https://fr.wikipedia.org/wiki/Chiffrement_par_d%C3%A9calage).

### Démonstration
https://appbrewery.github.io/python-day8-demo/

### À FAIRE-1: 
Créez une fonction appelée `encrypt()` qui prend `original_text` et `shift_amount` comme 2 entrées.

### À FAIRE-2: 
Dans la fonction 'encrypt', décalez chaque lettre du `original_text` vers l'avant dans l'alphabet du `shift_amount` et imprimez le texte chiffré.

Vous pouvez utiliser la fonction `index()` de Python pour trouver la position d'un élément dans une liste. par exemple:
```
fruits = ["Pomme", "Poire", "Orange"]
fruits.index("Poire") #1
```

par exemple. Si nous avons les valeurs suivantes :
```
plain_text = "bonjour"
shift_amount = 1
```
Le résultat final chiffré devrait être :

`Voici le résultat encodé : cpokpvs`

Où chaque lettre de 'bonjour' est décalée de 1. 

<div class="hint">
Décortiquons le problème :

  1. Vous avez besoin d'une boucle for pour parcourir chaque lettre du plain_text. 
  2. Trouvez la position de chaque lettre dans la Liste de l'alphabet.
3. Ajoutez le shift_amount souhaité par l'utilisateur à la position pour obtenir la position de la lettre codée.
4. Trouvez la lettre correspondante à cette position.
5. Ajoutez chaque lettre codée à une nouvelle chaîne et imprimez-la à la fin de la boucle.

</div>


### À FAIRE-3: 
Appelez la fonction `encrypt()` et transmettez les entrées de l'utilisateur. Vous devriez pouvoir tester le code et coder un message.


### À FAIRE-4: 
Que se passe-t-il si vous essayez de décaler la lettre 'z' vers l'avant de 9? Pouvez-vous corriger le code?

<div class="hint">
  Il existe de nombreuses approches pour cela.
1. Vous pouvez ajouter plus d'un ensemble de l'alphabet dans la Liste des lettres de l'alphabet.
2. Vous pouvez décaler le shift_amount pour qu'il soit toujours compris entre 0 et 25 et qu'il rentre dans la Liste.
3. Vous pouvez utiliser le modulo pour obtenir le reste.
</div>