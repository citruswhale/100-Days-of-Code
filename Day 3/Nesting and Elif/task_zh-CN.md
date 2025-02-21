### 嵌套条件语句
你可以将 if/else 语句放置在其他 if/else 语句中。这被称为嵌套。
例如：

```
if maths_score >= 90:
    if english_score >= 90:
        print("你擅长所有学科")
    else:
        print("你擅长数学")
if english_score >= 90:
    print("你擅长英语")
```

在这种情况下，只有当一名学生数学和英语成绩都超过90时，他们才会被评价为 "你擅长所有学科"。

注意：你也可以有不配对 else 语句的 if 语句。