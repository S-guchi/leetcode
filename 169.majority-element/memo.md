>Given an array nums of size n, return the majority element.

>The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.

>大きさnの配列numsが与えられたとき、多数派の要素を返す。

>多数決要素は、⌊n / 2⌋以上に出現する要素である。多数決の要素は常に配列中に存在すると仮定してよい。

- 配列の中から出現回数を調べる
```python
import collections
c = collections.Counter(nums) # 辞書になる
```

- 辞書の値が最大となるキーの取得方法
```python
max(c, key=c.get)
```