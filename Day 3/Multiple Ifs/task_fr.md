Vous pouvez écrire autant d'instructions if que nécessaire pour vérifier différentes conditions qui ne sont pas liées entre elles.
Comparez les blocs de code ci-dessous :
```
# If / elif / else
si <la condition 1 est vraie>
    <faites A>
elif <la condition 2 est vraie>
    <faites B>
else
    <faites C>
```
```
# Instructions if imbriquées
si <la condition 1 est vraie>
    <faites A>
    si <la condition 2 est vraie>
        <faites B>
        si <la condition 3 est vraie>
            <faites C>
```
```
# Plusieurs instructions if
if <la condition 1 est vraie>
    <faites A>
if <la condition 2 est vraie>
    <faites B>
if <la condition 3 est vraie>
    <faites C>
```

Dans le bloc if/elif/else, seulement l'une des options A, B ou C peut se produire, car if/elif/else sont mutuellement exclusifs. La première condition doit échouer pour entrer dans le elif et le elif (ou plusieurs elif) doit échouer pour passer à l'else. La condition 2 n'est vérifiée que si la condition 1 est fausse.

Dans les instructions if imbriquées, A, B et C peuvent tous se produire, mais les conditions 1, 2 et 3 doivent toutes être vraies. L'ordinateur ne vérifiera la condition 2 que si la condition 1 est vraie.

Dans les multiples instructions if, A, B et C peuvent tous se produire. Mais ils sont complètement indépendants les uns des autres. C peut se produire même si A et B ne se produisent pas. Chaque condition est vérifiée, peu importe le résultat des autres.