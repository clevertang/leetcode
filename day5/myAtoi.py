# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     myAtoi
   Description :
   Author :       tangxin
   date：          2018/7/19
-------------------------------------------------
   Change Activity:
                   2018/7/19:
-------------------------------------------------
"""
import re

"""
d第8题
"""


class Solution:
    # @return an integer
    def atoi(self, str):
        str = str.strip()
        str = re.findall('(^[\+\-0]*\d+)\D*', str)

        try:
            result = int(''.join(str))
            MAX_INT = 2147483647
            MIN_INT = -2147483648
            if result > MAX_INT > 0:
                return MAX_INT
            elif result < MIN_INT < 0:
                return MIN_INT
            else:
                return result
        except:
            return 0


if __name__ == '__main__':
    worker = Solution()
    s = "   -4193 with words123"
    worker.atoi(s)
