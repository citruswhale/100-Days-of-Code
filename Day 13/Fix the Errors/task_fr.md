Corrigez toutes les erreurs (soulignements rouges) qui apparaissent dans l'éditeur avant d'exécuter votre code. Les avertissements (jaunes) sont des corrections optionnelles, parfois cela causera un problème plus tard, d'autres fois c'est correct et l'éditeur ne comprend tout simplement pas ce que vous essayez de faire.

### Attraper Les Exceptions
Vous pouvez utiliser un bloc try/except en Python pour attraper toutes les exceptions qui pourraient se produire. Par exemple, si vous imaginez qu'il pourrait y avoir une chance d'erreur de l'utilisateur. Vous pouvez empêcher cela de faire planter votre code en l'anticipant. Vous bloquez le code dangereux à l'intérieur d'un bloc try et utilisez un bloc except pour attraper toutes les erreurs potentielles. Ensuite, vous définissez ce qui devrait se passer lorsque cette erreur se produit au lieu de simplement faire planter et arrêter le code.

par exemple.

```
try:
    print(6 > "five")
except TypeError:
    print("Vous ne pouvez pas mélanger des entiers et des chaînes de caractères dans une comparaison")
```

### PAUSE 1 
Corrigez le bogue afin que l'instruction d'impression affiche la valeur correcte de l'âge dans la zone de sortie.