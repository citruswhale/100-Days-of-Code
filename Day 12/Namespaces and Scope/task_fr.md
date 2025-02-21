### Portée Locale
Les variables (ou fonctions) déclarées à l'intérieur des fonctions ont une portée locale (également appelée portée de fonction). Elles ne sont vues que par d'autres codes dans le même bloc de code.

par exemple
```
def ma_fonction():
    ma_var_locale = 2
    
# Cela provoquera une NameErrorr
print(ma_var_locale) 
```

### Portée Globale
Les variables ou fonctions déclarées au niveau supérieur (indépendant) d'un fichier de code ont une portée globale. Elle est accessible partout dans le fichier de code.

par exemple

```
ma_var_globale = 3

def ma_fonction():
    # Cela fonctionne sans problème
    print(ma_var_globale)
```