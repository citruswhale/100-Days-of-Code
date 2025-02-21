函数在 `return` 关键字处终止。如果在 return 语句下面写代码，该代码将不会被执行。

但是，你可以在一个函数里有多个返回语句。那么，这是怎么运作的呢？

### 条件返回

当我们有控制流，就像代码会根据某些条件检查来呈现不同的行为（走不同的执行路径），我们可能会有多个结束（返回）。

例如：
```
def canBuyAlcohol(age):
    if age >= 18:
        return True
    else:
        return False
```

### 空返回
你也可以在 return 后面什么都不写，这就告诉函数要退出。

例如：
```
def canBuyAlcohol(age):
    # 如果 age 输入的数据类型不是 int，那么就退出。
    if type(age) != int:
        return

    if age >= 18:
        return True
    else:
        return False
```