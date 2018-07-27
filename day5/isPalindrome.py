# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     isPalindrome
   Description :
   Author :       tangxin
   date：          2018/7/19
-------------------------------------------------
   Change Activity:
                   2018/7/19:
-------------------------------------------------
"""


class Solution:
    # @param x, an integer
    # @return a boolean
    def isPalindrome(self, x):
        if x < 0:
            return False
        if x // 10 == 0:
            return True
        if x % 10 == 0:
            return False
        revertedNumber = 0
        while x > revertedNumber:
            revertedNumber = revertedNumber * 10 + x % 10
            x //= 10
        return x == revertedNumber or x == revertedNumber // 10


if __name__ == '__main__':
    worker = Solution()
    print(worker.isPalindrome(121))
