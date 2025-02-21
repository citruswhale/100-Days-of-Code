Vous pouvez utiliser les docstrings pour rédiger des commentaires multilignes qui documentent votre code.

### Syntaxe
Il suffit d'encadrer votre texte entre deux séries de trois guillemets doubles.

par exemple.
```
"""
Mon
Commentaire
Multiligne
"""

```

### Documentation des fonctions
Une fonctionnalité intéressante des docstrings est que vous pouvez les utiliser juste en dessous de la définition d'une fonction et que ce texte s'affichera lorsque vous survolez un appel de fonction. C'est une bonne façon de se rappeler ce qu'une fonction que vous avez créée fait.

par exemple.
```
def ma_fonction(num):
    """Multiplie un nombre par lui-même."""
    return num * num
```