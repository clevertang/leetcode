# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     longestPalindrome
   Description :
   Author :       tangxin
   date：          2018/7/18
-------------------------------------------------
   Change Activity:
                   2018/7/18:
-------------------------------------------------
"""


class Solution:

    def longestPalindrome(self, s):
        """
               :type s: str
               :rtype: str
               """
        res = ""
        for i in range(len(s)):
            tmp = self.helper(s, i, i)
            # odd case like aba
            if len(tmp) > len(res):
                res = tmp

            tmp = self.helper(s, i, i + 1)
            # even case like abba
            if len(tmp) > len(res):
                res = tmp
        return res

    # get the longest palindrome, l, r are the middle indexes
    # from inner to outer
    def helper(self, s, l, r):
        """

        :param s:
        :param l:
        :param r:
        :return:
        """
        while l >= 0 and r < len(s) and s[l] == s[r]:
            l -= 1
            r += 1
        print(s[l + 1:r])
        return s[l + 1:r]


if __name__ == '__main__':
    worker = Solution()
    s = 'caba'
    print(worker.longestPalindrome(s))
