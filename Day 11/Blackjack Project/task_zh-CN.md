### 选择你的难度
- **普通** 😎：使用以下所有提示完成项目。
- **困难** 🤔：只使用提示1、2、3来完成项目。
- **超级困难** 😭：仅使用提示1 & 2来完成项目。
- **专家** 🤯：仅使用提示1完成项目。

### 我们的二十一点游戏房规

- 牌堆的大小无限制。
- 没有大小王。
- 杰克/皇后/国王都算作10点。
- Ace可以算作11点或1点。
- 使用下面的列表作为牌堆：

`cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]`
- 列表中的牌被抽取的概率是相等的。
- 抽出的牌不会从牌堆中移除。
- 电脑是庄家。

<div class="hint" title="Hint 1">
  访问这个网站并试玩 Blackjack 游戏：

https://games.washingtonpost.com/games/blackjack/

然后再试试这里的已完成二十一点项目：

https://appbrewery.github.io/python-day11-demo/
</div>

<div class="hint" title="Hint 2">
阅读这个程序需求的分解：

http://listmoz.com/view/6h34DJpvJBFVRlZfJvxF

然后试着为程序构建你自己的流程图。

</div>

<div class="hint" title="Hint 3">
  下载并阅读我创建的这个流程图：

https://drive.google.com/uc?export=download&id=1rDkiHCrhaf9eX7u7yjM1qwSuyEk-rPnt

</div>

<div class="hint" title="Hint 4">
  创建一个 <code>deal_card()</code> 函数，使用下面的List返回一张随机牌。

<code>cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]</code>

记住其中的11代表 A牌。
</div>

<div class="hint" title="Hint 5">
  使用 <code>deal_card()</code> 和 <code>append()</code> 给用户和电脑各发两张牌。

<code>user_cards = []</code>

<code>computer_cards = []</code>
</div>

<div class="hint" title="Hint 6">
创建一个叫做<code>calculate_score()</code>的函数，让它以牌的列表作为输入，并返回所有牌的点数总和作为分数。你可以Google一下<code>sum()</code>函数来帮助你完成这一点。
</div>

<div class="hint" title="Hint 7">
在<code>calculate_score()</code>内部，检查是否有二十一点（一手只有两张牌： A + 10），返回<code>0</code>，而不是实际得分。 <code>0</code>将在我们的游戏中代表二十一点。
</div>

<div class="hint" title="Hint 8">
在<code>calculate_score()</code>内部，检查是否有11点（ace）。如果得分已经超过 21，将 11 去掉，用 1 替代。你可能需要 Google 查找 Python 内置函数 <code>append()</code> 和 <code>remove()</code> 的文档。

https://developers.google.com/edu/python/lists#list-methods
</div>

<div class="hint" title="Hint 9">
调用<code>calculate_score()</code>函数。如果电脑或用户有二十一点（0）或者用户的得分超过21，那么游戏结束。
</div>

<div class="hint" title="Hint 10">
如果游戏还没有结束，问用户是否想要再抽一张牌。如果是，那么使用<code>deal_card()</code>函数向<code>user_cards</code>列表中添加另一张牌。如果不是，那么游戏就结束了。
</div>

<div class="hint" title="Hint 11">
每次抽新牌后，都需要重新检查得分，并进行提示9中的检查，直到游戏结束。
</div>

<div class="hint" title="Hint 12">
一旦用户结束，就该让电脑开始游戏了。电脑应该一直抽牌，直到它的得分不小于17。
</div>

<div class="hint" title="Hint 13">
创建一个叫做<code>compare()</code>的函数，并传入<code>user_score</code> 和 <code>computer_score</code>。

- 如果电脑和用户得分相同，那就是平局。
- 如果电脑有二十一点（0），那么用户输了。
- 如果用户有二十一点（0），那么用户赢了。
- 如果<code>user_score</code>超过21，那么用户输了。
- 如果<code>computer_score</code>超过21，那么电脑输了。
- 如果以上都不满足，那么就看哪个玩家得分高。
</div>

<div class="hint" title="Hint 14">
问用户是否想要重启游戏。如果他们回答是的，清空控制台并开始新的二十一点游戏并显示来自 art.py 的 logo。
</div>