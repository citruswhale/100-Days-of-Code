### 待办事项-1: 
创建一个名为 `decrypt()` 的函数，该函数将 `original_text` 和 `shift_amount` 作为两个输入。

### 待办事项-2: 
在 `decrypt()` 函数中，使用 `shift_amount` 反向移动 `original_text` 中每个字母所对应的字母，并打印解密后的文本。

<div class="hint">
您可以将任何数字乘以 -1 以使其成为负数。
</div>


### 待办事项-3: 
- 将 `encrypt()` 和 `decrypt()` 函数合并成一个名叫 `caesar()` 的函数。
- 使用用户选择的 `direction` 变量值来确定使用哪个功能。
- 调用 caesar 函数而不是 encrypt/decrypt，并传入所有三个变量 `direction` / `text` / `shift`。

<div class="hint">
请记住，当您将一个数字乘以 -1 时，它的符号会反转。
例如，<code>3 + ( 5 * -1) </code> 与 <code>3 - 5</code> 是相同的。
</div>


<div class="hint">
它应该说:

<code>这是编码的结果: XXX</code>

或

<code>这是解码的结果: XXX</code> 

</div>