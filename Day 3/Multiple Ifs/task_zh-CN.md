您可以编写尽可能多的 if 语句来检查彼此无关的不同条件。
比较下面的代码块：
```
# If/elif/else
if <条件 1 为真>
    <执行 A>
elif <条件 2 为真>
    <执行 B>
else
    <执行 C>
```
```
# 嵌套 if 语句
if <条件 1 为真>
    <执行 A>
    if <条件 2 为真>
        <执行 B>
        if <条件 3 为真>
            <执行 C>
```

```
# 多个 if 语句
if <条件 1 为真>
    <执行 A>
if <条件 2 为真>
    <执行 B>
if <条件 3 为真>
    <执行 C>
```

在 if/elif/else 块中，只有 A、B 或 C 的其中一个可以发生，因为 if/elif/else 是互斥的。第一个条件必须失败，才能进入 elif，而 elif（或多个 elif）也必须失败才能进入 else。 只有当条件 1 为假时，才检查条件 2。

在嵌套的 if 语句中，A、B 和 C 都可以发生，但是条件 1、2 和 3 都必须为真。只有在条件 1 为真的情况下，计算机才会检查条件 2。

在多个 if 语句中， A、B、和 C 都可以发生。但是他们彼此完全独立。即使 A 和 B 不发生，C 也可以发生。每个条件都会被检查，无论其他结果如何。