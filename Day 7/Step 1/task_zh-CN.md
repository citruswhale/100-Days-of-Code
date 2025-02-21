你的目标是使用你所学的Python编程知识构建一个[猜单词游戏](https://en.wikipedia.org/wiki/Hangman_(game))。

### 演示最终项目
https://appbrewery.github.io/python-day7-demo/


该项目分为5个主要的步骤。在每个步骤中，都会有多个待完成事项（TODOs）。你的目标是按顺序完成每一个待完成事项。

你可以通过在PyCharm中点击View -> Tool Windows -> TODOs来轻松查看所有的待完成事项。

### TODO-1 
从`word_list`中随机选择一个词，并把它赋值给一个叫做`chosen_word`的变量。然后打印出来。

### TODO-2 
要求用户猜一个字母并把他们的答案赋值给一个叫做`guess`的变量。使存储在`guess`中的字符串小写。

<div class="hint">
  在Google中搜索Python中的lower()函数。
</div>


### TODO-3 
检查用户猜测的字母 `guess` 是否在 `chosen_word`中。循环遍历 `chosen_word` 中的每个字母, 如果字母匹配, 打印"正确", 如果不匹配, 打印"错误"。

<div class="hint">
  你可以使用 `for in` 循环来遍历字符串，就像遍历列表一样。
    尝试在Google中搜索："循环遍历字符串 python"
</div>