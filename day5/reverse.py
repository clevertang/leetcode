# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     reverse
   Description :
   Author :       tangxin
   date：          2018/7/19
-------------------------------------------------
   Change Activity:
                   2018/7/19:
-------------------------------------------------
"""
"""
第七题
"""


class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        flag = False
        if x < 0:
            flag = True
        if flag:
            sx = str(x).replace('-', '')
            sx = sx[::-1]
            result = -int(sx)
            if result < -pow(2, 31):
                result = 0
        else:
            result = int(str(x)[::-1])
            if result > pow(2, 31) - 1:
                result = 0
        return result
