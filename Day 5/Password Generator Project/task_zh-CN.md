程序将会询问：
```
您希望密码中有多少个字母？
您希望有多少个符号？
您希望有多少个数字？
```
目标是从用户对这些问题的输入中获取数据，然后生成一个随机密码。请运用你关于Python列表和循环的知识来完成这个挑战。

### 演示
https://appbrewery.github.io/python-day5-demo/

### 简单版本
依次生成密码。先是字母，然后是符号，最后是数字。如果用户想要

4个字母
2个符号和
3个数字
那么密码可能是这个样子：

`fgdx$*924`

你可以看到所有的字母在一起。所有的符号在一起，所有的数字也在一起。首先尝试解决这个问题。

<div class="hint">
  记住你可以使用random.choice()函数从列表中获取随机项！但是你需要先导入随机模块。
</div>


### 困难版本
当你完成简单版本后，就可以挑战困难版本了。在这个项目的高级版本中，最终的密码没有遵循任何模式。所以上面的例子可能看起来是这样的：

`x$d24g*f9`

每次你生成密码，符号、数字和字母的位置都是不同的。这将使密码更难以被黑客破解。

一个优秀的程序员最关键的技能是使用谷歌找到你所需的东西。你的大脑是用来思考的，不是用来记忆功能的！你将需要在谷歌上搜索解决这个项目的高难度级别。如果你卡住了，查看下面的提示，看看该谷歌什么。

<div class="hint">
  尝试谷歌搜索："如何在Python中混洗列表中的项目"
</div>