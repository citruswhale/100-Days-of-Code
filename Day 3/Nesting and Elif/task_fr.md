### Conditionnelles imbriquées
Vous pouvez mettre des instructions if/else à l'intérieur d'autres instructions if/else. C'est ce qu'on appelle l'imbrication.
par exemple

```
if maths_score >= 90:
    if english_score >= 90:
        print("Tu es doué en tout")
    else:
        print("Tu es doué en maths")
if english_score >= 90:
    print("Tu es doué en anglais)
```

Dans ce cas, seulement quand un étudiant a plus de 90 en maths et en anglais, ils obtiennent "Tu es doué en tout".

Note : Vous pouvez également avoir des instructions if qui n'ont pas une instruction else associée.