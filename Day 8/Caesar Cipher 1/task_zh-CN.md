你将使用[凯撒密码](https://en.wikipedia.org/wiki/Caesar_cipher)构建一个加密和解密程序。

### 示例
https://appbrewery.github.io/python-day8-demo/

### 待办事项-1: 
创建一个名为`encrypt()`的函数，该函数接受`original_text`和`shift_amount`作为两个输入。

### 待办事项-2: 
在'encrypt'函数内部，将`original_text`的每个字母按`shift_amount`向前移动，并打印加密文本。

你可以使用Python的内置`index()`函数来查找列表中项目的位置。例如：
```
fruits = ["Apple", "Pear", "Orange"]
fruits.index("Pear") #1
```

例如，如果我们有以下值：
```
plain_text = "hello"
shift_amount = 1
```
最后加密的输出应该是：

`这是编码结果：ifmmp`

其中，'hello'的每个字母都被提前1。

<div class="hint">
让我们分解一下问题：

  1. 你需要一个for循环来遍历plain_text中的每一个字母。
  2. 找到每个字母在字母表列表中的位置。
  3. 将用户想要的shift_amount加到位置上，得到编码字母的位置。
  4. 找到该位置对应的字母。
  5. 将每个编码字母添加到一个新的字符串中，然后在循环结束后打印出来。

</div>

### 待办事项-3: 
调用`encrypt()`函数，并传入用户的输入。你应该能测试代码并加密一条信息。

### 待办事项-4: 
如果你试图将字母'z'向前移动9步会发生什么？你能修复这个问题吗？

<div class="hint">
  有许多方法可以做到这一点。
1. 你可以在字母表的列表中添加不止一套字母表。
2. 你可以改变shift_amount，使其始终在0-25之间，且适合存入列表。
3. 你可以使用模数运算得到余数。
</div>