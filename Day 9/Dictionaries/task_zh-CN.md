Python中的字典的功能与现实生活中的字典类似。它是一种数据结构，使我们能够把一个键关联到一个值，并把这两部分数据配对在一起。

这是如何在Python中创建一个字典：
```
# 一个示例字典
colours = {
    "apple": "red", 
    "pear": "green", 
    "banana": "yellow"
}

```

这是如何从字典中取出项目：
```
print(colours["pear"])
#将打印 "green"
```

这是如何创建一个空字典：
```
my_empty_dictionary = {}
```

这是如何向现有字典中添加新项目：

```
colours["peach"] = "pink"
```

这也是如何编辑字典中的现有值：
```
colours["apple"] = "green"
```

这是如何遍历字典并打印所有的键：
```
for key in colours:
    print(key)
```

这是如何遍历字典并打印所有的值：
```
for key in colours:
    print(colours[key])
```