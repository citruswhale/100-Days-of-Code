### 类型错误
当你使用错误的数据类型时，这些错误会发生。
例如：`len(12345)`

因为你只能给`len()`函数提供字符串，如果你给它一个数字（整数）, 它将拒绝工作并给你一个类型错误。


#### 暂停1. 修复`len()`函数，使其没有更多的警告或错误。

### 类型检查
你可以使用`type()`函数检查任何值或变量的数据类型。

`print(type("abc")) #将给你 <class 'str'>`

#### 暂停2. 写出4个类型检查，以打印出所有4种数据类型
使用`type()`和`print()`函数打印出四行到输出区域，这样我们就可以得到我们学习过的所有数据类型的完整集合。`<class 'str'> <class 'int'> <class 'float'>和<class 'bool'>`

### 类型转换
你可以使用特殊函数将数据转换为不同的数据类型。
例如：

`float()` 

`int()`

`str()`

#### 暂停3. 让这行代码运行没有错误
`print("Number of letters in your name: " + len(input("Enter your name")))`