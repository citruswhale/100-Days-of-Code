### 伪随机数生成器
计算机并不是随机的，因为它们是由电路和开关构成的。但是在构建软件时，尤其是游戏，随机性非常重要。如果视频游戏的每一步动作都是预先决定的，那会非常无聊。

因此，一些计算机科学家发明了伪随机数生成器。例如：https://en.wikipedia.org/wiki/Mersenne_Twister

如果你想了解更多关于伪随机数生成器的信息，我推荐观看由可汗学院制作的这段视频：https://www.youtube.com/watch?v=GtOt7EBNEwQ&ab_channel=KhanAcademyLabs

### Python 中的 Random 模块
阅读文档详情：
https://docs.python.org/3/library/random.html

要使用它，首先需要导入：

`import random`

### 指定范围内的随机整数

```
import random
rand_num = random.randint(1, 10)

# 这段代码会生成一个范围在 1 到 10（包括 1 和 10）之间的随机整数。
```

### Python 中的模块
Python 允许我们将代码放入不同的文件中，并在需要时导入这些代码。这意味着我们可以更好地组织和模块化代码。

你可以通过创建一个新的 `.py` 文件来创建一个模块，然后只需使用 `import` 关键字，就可以从该文件中导入变量或函数。

### 随机浮点数
你可以使用 random 模块中的以下代码生成一个范围在 0.0（包括）到 1.0（不包括）之间的随机数：

```
import random
rand_num_0_to_1 = random.random()
```

它也可以表示为：

`0.0 <= random.random() < 1.0`

通过乘法操作，你可以扩展此方法生成的随机数的范围。

例如：`random.random() * 5`

会生成一个范围在 0 到 5 之间的随机数。

另一种生成随机浮点数的方法是使用 `uniform()` 函数。

```
import random
random_float = random.uniform(1, 10)
# 这段代码会生成一个范围在 1 到 10 之间的随机浮点数。
```

该方法可能会根据浮点数的舍入方式包含或不包含上限。因此最好表示为：

`a <= random.uniform(a,b) <= b`

因此，具体使用 `random.random()` 还是 `random.uniform()`，取决于你是否需要包含上限。

### 暂停 1：正面或反面
使用你在 Python 中关于随机化的学习内容，创建一个抛硬币的程序。每次运行程序时，它应随机打印“正面（Heads）”或“反面（Tails）”。

<div class="hint">
  你需要回忆一下关于 Python 条件语句的学习内容。
</div>