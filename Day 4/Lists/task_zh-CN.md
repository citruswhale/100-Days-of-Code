您可以使用 Python 的列表创建一个简单的有序项集合。例如：

`fruits = ["Cherry", "Apple", "Pear"]`

或者

`states_of_america = ["Delaware", "Pennsylvania", "New Jersey", "Georgia", "Connecticut", "Massachusetts", "Maryland", "South Carolina", "New Hampshire", "Virginia", "New York", "North Carolina", "Rhode Island", "Vermont", "Kentucky", "Tennessee", "Ohio", "Louisiana", "Indiana", "Mississippi", "Illinois", "Alabama", "Maine", "Missouri", "Arkansas", "Michigan", "Florida", "Texas", "Iowa", "Wisconsin", "California", "Minnesota", "Oregon", "Kansas", "West Virginia", "Nevada", "Nebraska", "Colorado", "North Dakota", "South Dakota", "Montana", "Washington", "Idaho", "Wyoming", "Utah", "Oklahoma", "New Mexico", "Arizona", "Alaska", "Hawaii"]`

### 访问列表中的项

您可以通过提供列表的名称，然后是方括号和您想要的项的索引来访问它。例如：

`states_of_america[0]`

将返回 "Delaware"。

请记住，在计算机相关的所有内容中，我们的计数从 0 开始，而不是 1。即是 0, 1, 2, 3 而不是 1, 2, 3, 4。

### 使用负索引

您可以通过使用负整数，从列表末尾开始访问列表中的项。例如：

```
fruits = ["Cherry", "Apple", "Pear"]
fruits[-1] # 结果是 "Pear"
```

### 修改列表中的项

您可以使用相同的语法获取列表中的项并对其进行修改。例如：

```
fruits = ["Cherry", "Apple", "Pear"]
fruits[0] = "Orange"
# fruits 现在将变为 ["Orange", "Apple", "Pear"]
```

### 添加列表项

您可以使用 `append()` 函数向列表末尾添加项。例如：

```
fruits = ["Cherry", "Apple", "Pear"]
fruits.append("Orange")
# fruits 现在将变为 ["Cherry", "Apple", "Pear", "Orange"]
```

### 列表的文档

您可以在以下链接中找到 Python 列表和其他与列表相关函数的文档：https://docs.python.org/3/tutorial/datastructures.html