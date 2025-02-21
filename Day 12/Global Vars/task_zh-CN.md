您可以通过在使用变量或对象之前使用global关键字，来强制代码允许您进行修改。

例如，以下的代码将会引发错误
```
a = 1
def my_function():
    a += 1
    print(a)
```

但下面的代码可以运行
```
a = 1
def my_function():
    global a
    a += 1
    print(a)
```