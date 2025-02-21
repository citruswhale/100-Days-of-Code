### TypeError
Ces erreurs se produisent lorsque vous utilisez le mauvais type de données.
Par exemple : `len(12345)`

Comme vous ne pouvez donner à la fonction `len()` que des Strings, elle refusera de fonctionner et vous donnera une erreur de type TypeError si vous lui donnez un nombre (Integer).


#### PAUSE 1. Corrigez la fonction `len()` pour qu'elle n'ait plus d'avertissements ni d'erreurs.

### Vérification du type
Vous pouvez vérifier le type de données de n'importe quelle valeur ou variable en Python en utilisant la fonction `type()`.

`print(type("abc")) #donnera <class 'str'>`

#### PAUSE 2. Écrivez 4 contrôles de type pour imprimer les 4 types de données
En utilisant les fonctions `type()` et `print()` pour imprimer 4 lignes dans la zone de sortie afin que nous obtenions la collection complète de types de données que nous avons appris. `<class 'str'> <class 'int'> <class 'float'> et <class 'bool'>`

### Conversion de type
Vous pouvez convertir les données en différents types de données à l'aide de fonctions spéciales.
Par exemple :

`float()`

`int()`

`str()`

#### PAUSE 3. Faites en sorte que cette ligne de code s'exécute sans erreurs
`print("Nombre de lettres dans votre nom : " + len(input("Entrez votre nom")))`