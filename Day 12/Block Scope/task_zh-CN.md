Python与其他编程语言有些不同，它没有块范围。

这意味着在其他代码块（例如for循环、if语句、while循环等）中创建的变量不具有局部范围。如果它们在函数中，则赋予函数范围，如果不在，则赋予全局范围。

例如

```
# 可在任何地方访问
my_global_var = 1

def my_function():
    # 只能在my_function()内访问
    my_local_var = 2
    
for _ in range(10):
    # 可在任何地方访问
    my_block_var = 3

```