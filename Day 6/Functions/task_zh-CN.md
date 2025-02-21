一个函数在最简单的形式下只是代码块的一个包装名称。你给它一个名字，然后当你通过这个名字调用函数时，函数块中的所有代码都会被执行。它可以帮助我们节省时间并减少重复的代码。

### 定义一个新函数
```
def <函数名>():
    print("Hello")
    # 执行其他操作
    # 执行其他操作 ...
```

### 调用一个函数
调用一个函数只是指触发该函数。我们可以在 Python 的代码中随时调用一个函数。

```
<函数名>()
```

将所有部分整合在一起，例如：
```
# 创建函数
def get_user_name():
    name = input("What is your name? ")
    print("Hello, " + name)
    # 函数内部的操作

# 函数外部的操作
print("Hello")
get_user_name() # 调用函数
```

此代码将产生以下输出顺序：
```
Hello
What is your name? # 我输入 Angela
Hello
Angela