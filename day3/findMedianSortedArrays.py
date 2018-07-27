# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     findMedianSortedArrays
   Description :
   Author :       tangxin
   date：          2018/7/17
-------------------------------------------------
   Change Activity:
                   2018/7/17:
-------------------------------------------------
"""


class Solution:
    @staticmethod
    def findMedianSortedArrays(nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        m, n = len(nums1), len(nums2)
        if m + n == 0:
            return 0
        flag = 1 if (m + n) & 1 == 1 else 0
        mid = (m + n) // 2
        l1 = l2 = count = 0
        L = []
        while l1 < m and l2 < n and count <= mid:
            if nums1[l1] > nums2[l2]:
                L.append(nums2[l2])
                l2 += 1
            else:
                L.append(nums1[l1])
                l1 += 1
            count += 1
        while l1 < m and count <= mid:
            L.append(nums1[l1])
            l1 += 1
            count += 1
        while l2 < n and count <= mid:
            L.append(nums2[l2])
            l2 += 1
            count += 1
        return L[mid] / 1. if flag else (L[mid] + L[mid - 1]) / 2.


if __name__ == '__main__':
    s1 = []
    s2 = [1]
    print(Solution.findMedianSortedArrays(s1, s2))
