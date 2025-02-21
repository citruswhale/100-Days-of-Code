### TODO-1: 
Créez une fonction appelée `decrypt()` qui prend `original_text` et `shift_amount` comme 2 entrées.

### TODO-2: 
À l'intérieur de la fonction `decrypt()`, décalez chaque lettre du `original_text` en avant dans l'alphabet *en arrière* par le `shift_amount` et imprimez le texte déchiffré.

<div class="hint">
  Vous pouvez multiplier n'importe quel nombre par -1 pour en faire un nombre négatif.
</div>


### TODO-3: 
- Combinez les fonctions `encrypt()` et `decrypt()` en une seule fonction appelée `caesar()`. 
- Utilisez la valeur de la variable `direction` choisie par l'utilisateur pour déterminer quelle fonctionnalité utiliser. 
- Appelez la fonction caesar à la place de encrypt/decrypt et transmettez les trois variables `direction`/`text`/`shift`.

<div class="hint">
  Souvenez-vous que lorsque vous multipliez un nombre par -1, son signe s'inverse.
par ex. <code>3 + ( 5 * -1) </code> est la même chose que <code>3 - 5</code>.
</div>


<div class="hint">
Il devrait dire:  

<code>Voici le résultat encodé: XXX</code>

ou

<code>Voici le résultat décodé: XXX</code> 

</div>