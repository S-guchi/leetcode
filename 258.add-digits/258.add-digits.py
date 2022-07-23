#
# @lc app=leetcode id=258 lang=python3
#
# [258] Add Digits
#

# @lc code=start
from unittest import result


class Solution:
    def addDigits(self, num: int) -> int:
        # ary = []
        # while True:
        #     result = 0
        #     for i in range(len(str(num))):
        #         num, surplus = divmod(num, 10)
        #         result = result + surplus

        #     if result >= 10:
        #         num = result
        #     else:
        #         break
        # return result
        if num == 0:
            return 0
        if num % 9 == 0:
            return 9
        else:
            return num % 9


# @lc code=end

S = Solution()
print(S.addDigits(19))
