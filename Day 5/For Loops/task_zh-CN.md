循环让我们能够指示计算机重复执行某些操作，而无需重复编写代码。如果我们希望计算机打印出从 1 到 100 的数字，那么为每个数字书写一条打印语句会非常麻烦，甚至手动输入所有从 1 到 100 的数字也是如此。循环允许我们创建一条规则，计算机可以遵循这条规则来执行重复的操作。

### 语法

```
for <每项内容的变量名> in <一个列表>:
    <执行某些操作>
    <执行其他操作>
```

### 暂停 1 - 化身为计算机
预测以下代码会打印出什么：

```
fruits = ["Apple", "Peach", "Pear"]
for fruit in fruits:
    print(fruit)
    print(fruit + " pie")
```

### 缩进
在 Python 编程中，缩进非常重要。每次你看到使用 `:` 的符号时，你需要特别注意随后代码的缩进。

例如：以下代码的行为非常不同：

```
fruits = ["Apple", "Peach", "Pear"]
for fruit in fruits:
    print(fruit)
    print("Hello")
```

与这段代码：

```
fruits = ["Apple", "Peach", "Pear"]
for fruit in fruits:
    print(fruit)
print("Hello")