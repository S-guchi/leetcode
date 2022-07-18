# memo

- https://youtu.be/KLlXCFG5TnA
解説に載っていたコード
ハッシュを使う
targetからvalueを引きdiff配列に入れて、
if diff in prevMap:で　prevMapをチェックして、valueが含まれていたら
足した数がtargetになる要素が見つかったってことになる

```
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevMap = {}  # val:index
       for i, n in enumerate(nums):
            diff = target - n
            if diff in prevMap:
                return [prevMap[diff], i]
            prevMap[n] = i
        return
```