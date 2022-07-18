#
# @lc app=leetcode id=1 lang=python3
#
# [1] Two Sum
#
# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
# You can return the answer in any order.

# 整数numsの配列と整数targetが与えられたとき、2つの数値の足し算がtargetになるようなインデックスを返せ。

# 各入力は正確に1つの解を持つと仮定してよく、同じ要素を2度使ってはならない。

# また、同じ要素を2度使ってはならない。解答はどのような順序でも返すことができる。


# @lc code=start
# from black import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        for xi in range(len(nums)):
            for yi in range(xi + 1, len(nums)):
                if (nums[xi] + nums[yi]) == target:
                    return [xi, yi]


# https://youtu.be/KLlXCFG5TnA
# 解説に載っていたコード
# ハッシュを使う
# targetからvalueを引きdiff配列に入れて、
# if diff in prevMap:で　prevMapをチェックして、valueが含まれていたら
# 足した数がtargetになる要素が見つかったってことになる
# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#         prevMap = {}  # val:index
#         for i, n in enumerate(nums):
#             diff = target - n
#             if diff in prevMap:
#                 return [prevMap[diff], i]
#             prevMap[n] = i
#         return

# @lc code=end


s = Solution()
print(s.twoSum(nums=[4, 2, 1], target=5))
