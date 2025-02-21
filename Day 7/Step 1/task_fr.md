Votre objectif est de construire un [jeu de pendu](https://fr.wikipedia.org/wiki/Le_Pendu_(jeu)) en utilisant tout ce que vous avez appris sur la programmation Python.

### Démonstration du Projet Final
https://appbrewery.github.io/python-day7-demo/

Le projet est divisé en 5 étapes majeures. Dans chaque étape, il y aura plusieurs TODOs. Votre objectif est de passer par chaque todo dans l'ordre et de les compléter.

Vous pouvez voir tous les todos facilement dans PyCharm en allant à Afficher -> Fenêtres d'outils -> TODOs

### TODO-1 
Choisissez aléatoirement un mot de la `word_list` et attribuez-le à une variable appelée `chosen_word`. Ensuite, imprimez-le.

### TODO-2 
Demandez à l'utilisateur de deviner une lettre et attribuez leur réponse à une variable appelée `guess`. Faites en sorte que la chaîne de caractères stockée dans `guess` soit en minuscules.

<div class="hint">
  Cherchez sur Google la fonction lower() en Python.
</div>

### TODO-3 
Vérifiez si la lettre que l'utilisateur a deviné `guess` est l'une des lettres du `chosen_word`. Parcourez chacune des lettres de `chosen_word` et imprimez "Correct" si la lettre correspond, "Incorrect" si ce n'est pas le cas.

<div class="hint">
  Vous pouvez parcourir les chaînes de caractères de la même manière que vous pouvez parcourir les listes - en utilisant la boucle `for in`.
Essayez de chercher sur Google : "Parcourir les chaînes de caractères en python"
</div>