Vous pouvez forcer le code à vous permettre de modifier quelque chose avec global si vous utilisez le mot-clé global avant de l'utiliser.

Par exemple, cela vous donnera une erreur

```
a = 1
def ma_fonction():
    a += 1
    imprimer(a)
```

Mais ça marchera
```
a = 1
def ma_fonction():
    global a
    a += 1
    imprimer(a)
```