### 待办事项-1： 
当程序开始时，从 art.py 中导入并打印图标。

### 待办事项-2： 
如果用户输入的数字/符号/空格不在列表`alphabet`中会发生什么？

你能修复代码以在文本被编码/解码时保留数字/符号/空格吗？

例如 
```
original_text = "meet me at 3!"
cipher_text = "XXXX XX XX 3!"
```

<div class="hint">
  如果不是列表 alphabet 中的字母，也许你可以将它作为未修改的字符加到 cipher_text 的末尾？
</div>


### 待办事项-3： 

你能找到一种方法重启密码程序吗？

例如 

`如果你想再走一遍，输入'yes'。否则，输入'no'。`

如果他们输入'yes'，那么再次向他们询问方向/文字/移位，并再次调用 `caesar()` 函数。

<div class="hint">
  尝试创建一个 while 循环，如果用户输入 'yes' 则继续执行程序。
</div>