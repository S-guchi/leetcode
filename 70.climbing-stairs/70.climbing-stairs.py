#
# @lc app=leetcode id=70 lang=python3
#
# [70] Climbing Stairs
#

# @lc code=start
class Solution:
    def climbStairs(self, n: int) -> int:
        one, two = 1, 1
        for i in range(n - 1):
            tmp = one
            one = one + two
            two = tmp

        return one


# @lc code=end

a = Solution()
print(a.climbStairs(5))
