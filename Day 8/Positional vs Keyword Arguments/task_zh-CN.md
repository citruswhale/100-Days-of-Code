### 多个输入
您可以在函数中拥有多个输入。您只需要用逗号`,`将它们隔开。

### 停顿 1
创建一个具有多个输入的函数

<div class="hint">
  <code>
def greet(name, greeting):

    ____print(f"{greeting} {name}")
    
greet("Angela", "Yo!")
</code>
</div>

### 停顿 2
修改函数，使其打印预期的值。
```
def greet_with(name, location)
    Hello name
    What is it like in location
```

### 位置参数
默认情况下，当您在Python中创建函数时，它会保留函数定义中的参数顺序。

例如，在下面的函数中，第一个进入的参数将始终在第二个之前打印。`a = 2, b = 1`

```
def my_function(a, b)
  print(a)
  print(b)
  
 my_function(2, 1)
 #它将打印：
 # 2
 # 1
```

### 关键字参数
在调用函数提供参数时，您可以使用关键词，以便减少对输入参数值分配的混淆。

### 停顿 3
使用关键字参数调用`greet_with()`函数。

<div class="hint">
  <code>
greet_with(location="London", name="Angela")
</code>
</div>