### Choisissez votre difficulté
- **Normal** 😎: Utilisez tous les indices ci-dessous pour terminer le projet.
- **Difficile** 🤔: Utilisez seulement les indices 1, 2, 3 pour terminer le projet.
- **Très difficile** 😭: Utilisez uniquement les indices 1 et 2 pour terminer le projet.
- **Expert** 🤯: Utilisez uniquement l'indice 1 pour terminer le projet.

### Nos règles du jeu Blackjack

- Le paquet est illimité en taille.
- Il n'y a pas de jokers.
- Le Valet, la Dame, le Roi comptent tous comme 10.
- L'As peut compter comme 11 ou 1.
- Utilisez la liste suivante comme le paquet de cartes :

`cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]`
- Les cartes de la liste ont une probabilité égale d'être tirées.
- Les cartes ne sont pas retirées du paquet lorsqu'elles sont tirées.
- L'ordinateur est le croupier.

<div class="hint" title="Indice 1">
Allez sur ce site et essayez le jeu Blackjack:

https://games.washingtonpost.com/games/blackjack/

Puis essayez le projet Blackjack terminé ici:

https://appbrewery.github.io/python-day11-demo/
</div>

<div class="hint" title="Indice 2">
Lisez cette répartition des exigences du programme:

http://listmoz.com/view/6h34DJpvJBFVRlZfJvxF

Essayez ensuite de créer votre propre diagramme de flux pour le programme.
</div>

<div class="hint" title="Indice 3">
Téléchargez et lisez ce diagramme de flux que j'ai créé:

https://drive.google.com/uc?export=download&id=1rDkiHCrhaf9eX7u7yjM1qwSuyEk-rPnt
</div>

<div class="hint" title="Indice 4">
Créez une fonction <code>deal_card()</code> qui utilise la liste ci-dessous pour retourner une carte aléatoire.

<code>cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]</code>

Rappelez-vous que 11 est l'As.
</div>

<div class="hint" title="Indice 5">
Donnez à l'utilisateur et à l'ordinateur 2 cartes chacun en utilisant <code>deal_card()</code> et <code>append()</code>.

<code>user_cards = []</code>

<code>computer_cards = []</code>
</div>

<div class="hint" title="Indice 6">
Créez une fonction appelée <code>calculate_score()</code> qui prend une liste de cartes en entrée et retourne la somme de toutes les cartes de la liste comme le score. Cherchez la fonction <code>sum()</code> pour vous aider à faire cela.
</div>

<div class="hint" title="Indice 7">
Dans <code>calculate_score()</code> vérifiez s'il y a un blackjack (une main de seulement 2 cartes : as + 10) et retournez <code>0</code> au lieu du score réel. <code>0</code> représentera un blackjack dans notre jeu.
</div>

<div class="hint" title="Indice 8">
Dans <code>calculate_score()</code> vérifiez s'il y a un 11 (as). Si le score est déjà supérieur à 21, retirez le 11 et remplacez-le par un 1. Vous pourriez avoir besoin de chercher sur Google pour trouver la documentation sur les fonctions intégrées de Python <code>append()</code> et <code>remove()</code>.

https://developers.google.com/edu/python/lists#list-methods
</div>

<div class="hint" title="Indice 9">
Appelez la fonction<code>calculate_score()</code>. Si l'utilisateur ou l'ordinateur ont un blackjack (0) ou si le score de l'utilisateur est supérieur à 21, alors le jeu se termine.
</div>

<div class="hint" title="Indice 10">
Si le jeu n'est pas terminé, demandez à l'utilisateur s'il veut tirer une autre carte. Si oui, utilisez la fonction <code>deal_card()</code> pour ajouter une autre carte à la liste <code>user_cards</code>. Si non, alors le jeu est terminé.
</div>

<div class="hint" title="Indice 11">
Le score doit être revérifié à chaque nouvelle carte tirée et les vérifications indiquées à l'indice 9 doivent être répétées jusqu'à ce que le jeu se termine.
</div>

<div class="hint" title="Indice 12">
Une fois que l'utilisateur a fini, c'est au tour de l'ordinateur de jouer. L'ordinateur doit continuer à tirer des cartes tant que son score est inférieur à 17.
</div>

<div class="hint" title="Indice 13">
Créez une fonction appelée <code>compare()</code> et passez <code>user_score</code> et <code>computer_score</code>.

- Si l'ordinateur et l'utilisateur ont le même score, alors c'est un match nul.
- Si l'ordinateur a un blackjack (0), alors l'utilisateur perd.
- Si l'utilisateur a un blackjack (0), alors l'utilisateur gagne.
- Si le <code>user_score</code> est supérieur à 21, alors l'utilisateur perd.
- Si le <code>computer_score</code> est supérieur à 21, alors l'ordinateur perd.
- Si aucune des conditions ci-dessus n'est remplie, alors le joueur avec le score le plus élevé gagne.
</div>

<div class="hint" title="Indice 14">
Demandez à l'utilisateur s'il veut redémarrer le jeu. S'ils répondent oui, effacez la console et commencez une nouvelle partie de blackjack et montrez le logo de art.py.
</div>