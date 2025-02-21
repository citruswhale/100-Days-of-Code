### Somme
Python a beaucoup de fonctions intégrées pour nous aider à travailler avec des chiffres. Une d'entre elles nous aide à calculer la somme (le total).
par exemple.
```
student_scores = [180, 124, 165, 173, 189, 169, 146]
total_score = sum(student_scores) 
```
Mais comment `sum()` fonctionne-t-elle en coulisse ? Le code est écrit par les personnes qui ont développé Python et il pourrait ressembler à quelque chose comme ça:

```
student_scores = [180, 124, 165]

sum = 0
for score in student_scores:
    sum += score
    
print(sum)
```



### PAUSE 1 - Max
Il existe également des méthodes Python intégrées appelées `max()` and `min()`, qui vous permettent de passer une liste de chiffres, et il vous donnera le chiffre le plus élevé ou le plus bas.

Votre travail consiste à comprendre comment les programmeurs Python auraient pu construire cette fonctionnalité en utilisant des boucles et des conditionnels.

## COMPLETEZ CE DEFI SANS UTILISER max()

On vous donne une liste de notes d'examen, et vous devez imprimer la note la plus élevée de la liste.
Vous devrez utiliser ce que vous avez appris sur les listes, les boucles For et les conditionnels pour imprimer la note la plus élevée dans la liste des student_scores.
Par exemple, si les scores étaient :
```
8 65 89 86 55 91 64 89
```
Votre code devrait imprimer
```
91
```