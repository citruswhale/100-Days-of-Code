### 列表的长度
您可以使用 `len()` 函数获取列表的长度（列表中项目的数量）或字符串的长度（字符串中字符的数量）。https://docs.python.org/3/library/functions.html#len

### 索引错误 (IndexError)
当您尝试访问列表中不存在范围的项目时，会得到一个索引错误 (IndexError)。例如：

```
fruits = ["Cherry", "Apple", "Pear"]
print(fruits[3]) #这会导致一个索引错误 (IndexError)
```

### 嵌套列表
您可以将一个列表放入另一个列表中，这种结构被称为“嵌套列表”或“二维列表”。例如：

```
fruits = ["Cherry", "Apple", "Pear"]
veg = ["Cucumber", "Kale", "Spinnach"]
fruits_and_veg = [fruits, veg]
#这个列表看起来是这样的: [["Cherry", "Apple", "Pear"], ["Cucumber", "Kale", "Spinnach"]]
```
您还可以像这样以二维格式表示列表：
```
["Cherry", "Apple", "Pear"]
["Cucumber", "Kale", "Spinnach"]