# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     lengthOfLongestSubstring
   Description :
   Author :       tangxin
   date：          2018/7/17
-------------------------------------------------
   Change Activity:
                   2018/7/17:
-------------------------------------------------
"""
from collections import deque


class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0
        x = []
        a = 0
        for i in s:
            if i in x:  # Once there is a repetition
                if len(x) > a:
                    a = len(x)
                del x[:x.index(i) + 1]  # We delete the repeated one and all before it
            x.append(i)
        return max(a, len(x))


if __name__ == '__main__':
    worker = Solution()

    string = "abcbbc"
    print(worker.lengthOfLongestSubstring(string))
