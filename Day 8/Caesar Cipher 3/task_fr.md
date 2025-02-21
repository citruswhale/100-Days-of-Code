### ÀFAIRE-1: 
Importez et imprimez le logo à partir de art.py lorsque le programme démarre.

### ÀFAIRE-2: 
Que se passe-t-il si l'utilisateur entre un numéro/symbole/espace qui n'est pas dans la liste `alphabet`?

Pouvez-vous corriger le code pour conserver le numéro/symbole/espace lorsque le texte est codé/décodé?

par exemple 
```
texte_original = "rendez-vous à 3!"
texte_chiffré = "XXXX-XXX-XX 3!"
```

<div class="hint">
  Si ce n'est pas une lettre dans la liste alphabet, peut-être que vous pouvez simplement l'ajouter à la fin du texte_chiffré en tant que caractère non modifié?
</div>

### ÀFAIRE-3: 

Pouvez-vous trouver un moyen de redémarrer le programme de chiffrement?

par exemple 

`Tapez 'oui' si vous voulez recommencer. Sinon, tapez 'non'.`

S'ils tapent 'oui', demandez-leur à nouveau la direction/le texte/le décalage et appelez à nouveau la fonction `caesar()`.

<div class="hint">
  Essayez de créer une boucle while qui continue à exécuter le programme si l'utilisateur tape 'oui'.
</div>