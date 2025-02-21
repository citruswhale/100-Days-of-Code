La combinaison de la fonction `range()` avec la boucle For de Python nous permet d'exécuter une boucle autant de fois que nous le souhaitons. Au lieu de boucler à travers chaque élément d'une liste, nous pouvons boucler à travers une plage de nombres.

### Fonction Range

`range(1, 10)`

Ce code ne fait rien par lui-même. Par exemple, si vous essayiez de l'imprimer, il ne vous donnerait pas de nombres individuels.

Mais il peut être utilisé en conjonction avec les Boucles For. Par exemple,

```
for number in range(1, 10):
    print(number)
```

Cela imprimera chacun des nombres de 1 à 9. Ainsi, la plage peut également être exprimée de cette façon :

`a <= range(a, b) < b`

Où la plage de nombres est inclusive de la borne inférieure mais non inclusive de la borne supérieure.

### PAUSE 1 - Le Défi Gauss
Calculez le total des nombres entre 1 et 100, inclusivement 1 et 100.
