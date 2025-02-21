### 待办事项-1
- 创建一个名为 `placeholder`的空字符串。
- 在 `chosen_word`的每个字母中，将一个`_`添加到`placeholder`中。
- 所以如果`chosen_word`是"apple"，那么`placeholder`应该是`_ _ _ _ _`，有5个`"_"`代表每个要猜测的字母。
- 打印出`hint`。

<div class="hint">
  请记住，您可以在循环内使用range()函数执行特定次数的操作。 
</div>


### 待办事项-2
- 创建一个名为"display"的空字符串。
- 循环遍历 `chosen_word`的每个字母
- 如果该位置的字母与 `guess`相匹配，则在那个位置的 `display`中揭示该字母。
- 例如，如果用户猜测的是"p"并且选择的词是"apple"，那么 `display`应该是`_ p p _ _`。
- 打印 `display`，您应该在正确位置看到猜测的字母。
- 但是，每个不匹配的字母都用"_"表示。

<div class="hint">
  请记住，for循环将按顺序遍历 chosen_word中的每个字母。 您可以利用这个事实来创建一个新的字符串，添加字母或"_"
</div>