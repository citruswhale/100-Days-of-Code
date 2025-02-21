### TODO-1
- Créez une chaîne vide appelée `placeholder`.
- Pour chaque lettre du `mot_choisi`, ajoutez un `_` au `placeholder`.
- Donc, si le `mot_choisi` était "pomme", `placeholder` devrait être `_ _ _ _ _` avec 5 `"_"` représentant chaque lettre à deviner.
- Imprimez `hint`.

<div class="hint">
  Rappelez-vous que vous pouvez utiliser la fonction range() à l'intérieur d'une boucle pour effectuer une action un certain nombre de fois.
</div>


### TODO-2
- Créez une chaîne vide appelée "affichage".
- Parcourez chaque lettre du `mot_choisi`.
- Si la lettre à cette position correspond à `devinette`, alors révélez cette lettre dans l' `affichage` à cette position.
- Par exemple, si l'utilisateur a deviné "p" et que le mot choisi était "pomme", alors l' `affichage` devrait être `_ p _ _ _`.
- Imprimez `affichage` et vous devriez voir la lettre devinée à la bonne position.
- Mais chaque lettre qui ne correspond pas est représentée par un "_".

<div class="hint">
  N'oubliez pas que la boucle for va parcourir chaque lettre du mot_choisi dans l'ordre. Vous pouvez utiliser ce fait pour créer une nouvelle chaîne, en ajoutant la lettre ou un "_".
</div>