#
# @lc app=leetcode id=169 lang=python3
#
# [169] Majority Element
#
import collections

from black import List

# @lc code=start
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        c = collections.Counter(nums)
        d = max(c, key=c.get)  # Key with the largest dictionary value
        return d


# @lc code=end

s = Solution()
print(s.majorityElement([2, 2, 1, 1, 1, 1, 3, 2, 3]))
