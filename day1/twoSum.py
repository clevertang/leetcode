# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     twoSum
   Description :
   Author :       tangxin
   date：          2018/7/13
-------------------------------------------------
   Change Activity:
                   2018/7/13:
-------------------------------------------------
"""


class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if len(nums) <= 1:
            return False
        buff_dict = {}
        for i in range(len(nums)):
            if nums[i] in buff_dict:
                return [buff_dict[nums[i]], i]
            else:
                buff_dict[target - nums[i]] = i


if __name__ == '__main__':
    worker = Solution()
    a = [3, 1, 3, 2]
    s = 5
    print(worker.twoSum(a, s))
