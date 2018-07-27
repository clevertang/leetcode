# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     another
   Description :
   Author :       tangxin
   date：          2018/7/19
-------------------------------------------------
   Change Activity:
                   2018/7/19:
-------------------------------------------------
"""


class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """

        if s == '':
            return 0

        M = 1
        left = right = 0
        idxs = [0, 1]
        for i in range(1, len(s)):
            new_idxs = [i, i + 1]
            for idx in idxs:
                if idx - 1 >= 0 and s[i] == s[idx - 1]:
                    new_idxs.append(idx - 1)
                    length = i - (idx - 1) + 1
                    if M < length:
                        left = idx - 1
                        right = i
                        M = length
            idxs = new_idxs

        return s[left:right + 1]


if __name__ == '__main__':
    woker = Solution()
    s = 'babad'
    print(woker.longestPalindrome(s))
