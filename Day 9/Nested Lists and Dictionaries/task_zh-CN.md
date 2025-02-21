您可以混合并匹配各种数据类型以实现您想要的结构。

### 在字典中嵌套列表
我们可以用列表来替换分配给键的字符串值。这样就可以在字典中嵌套一个列表：

```
my_dictionary = {
    key1: [列表],
    key2: 值,
}
```

### 暂停 1
看看您是否可以找出如何从名为 `travel_log`的嵌套列表中打印出 "Lille"。
```
travel_log = {
    "France": ["Paris", "Lille", "Dijon"],
    "Germany": ["Stuttgart", "Berlin"],
}
```
<div class="hint">
  要获取这部分：<code>["Paris", "Lille", "Dijon"]</code>
你需要：<code>travel_log["France"]</code>

因此，要得到Lille，你需要：
<code>travel_log["France"][1]</code>
</div>

### 在其他列表中嵌套列表

我们之前已经看到了嵌套列表：

```
nested_list = ["A", "B", ["C", "D"]]
```

### 暂停 2
您还记得如何获取深层嵌套在列表中的项目吗？尝试从 `nested_list` 列表中打印 "D"。

<div class="hint">
  要得到这个列表：["C", "D"]，我们需要代码：

<code>nested_list[2]</code>

因此，要得到 "D"，我们需要：

<code>nested_list[2][1]</code>
</div>

### 在字典中嵌套字典
您也可以在字典中嵌套一个字典：

```
my_dictionary = {
    key1: 值,
    key2: {键: 值, 键: 值},
}
```

### 暂停 3
找出如何从下列列表中打印出 "Stuttgart"：
```
travel_log = {
  "France": {
    "cities_visited": ["Paris", "Lille", "Dijon"], 
    "total_visits": 12
   },
  "Germany": {
    "cities_visited": ["Berlin", "Hamburg", "Stuttgart"], 
    "total_visits": 5
   },
}
```