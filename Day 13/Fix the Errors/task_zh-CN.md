在运行代码之前，请修复出现在编辑器中的任何错误（红线）。警告（黄色）属于可选修复，有时可能会引发之后的问题，有时它可以运行良好，编辑器只是不理解你想做什么。

###捕获异常
你可以在Python中使用try/except语句块来捕获可能发生的任何异常。例如，你预想到可能会有用户错误。通过预见到这点，可以阻止代码崩溃。你需要将危险的代码封装在 try 语句块中，并使用except语句块来捕捉任何可能的错误。然后你定义发生错误时应有哪些行动，而不只是简单地崩溃并停止代码。

例如：

```
try:
    print(6 > "five")
except TypeError:
    print("你不能在比较中混合整数和字符串")
```

###暂停 1 
修复这个bug，以便打印语句在输出区域显示年龄的正确值。