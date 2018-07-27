# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     addTwoNumbers
   Description :
   Author :       tangxin
   date：          2018/7/14
-------------------------------------------------
   Change Activity:
                   2018/7/14:
-------------------------------------------------
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class LinkList(object):
    def __init__(self):
        self.head = ListNode(0)

    def initlist(self):

        print("input numbers here.'!' to quit")

        data = input()
        if data is not '-1':
            self.head = ListNode(int(data))
        p = self.head
        while data != '-1':
            data = input()
            if data == '-1':
                break
            else:
                p.next = ListNode(int(data))
                p = p.next

        print("输入结束！")


class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        res = ListNode(0)
        first = res
        add = False
        while l1 or l2 or add:
            if l1 is None:
                x = 0
            else:
                x = l1.val
                l1 = l1.next
            if l2 is None:
                y = 0
            else:
                y = l2.val
                l2 = l2.next

            res.next = ListNode(x + y)
            res = res.next
            if add:
                res.val += 1
                add = False
            if res.val > 9:
                res.val -= 10
                add = True

        return first.next


if __name__ == '__main__':
    worker = Solution()
    # s1 = LinkList()
    # s1.initlist()
    # s2 = LinkList()
    # s2.initlist()
    s1 = ListNode(3)
    s1.next = ListNode(5)
    s2 = ListNode(8)
    s2.next = ListNode(1)
    worker.addTwoNumbers(s1, s2)
