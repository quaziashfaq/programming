#!/usr/bin/env python3

from typing import *

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def print(self):
        temp = self
        while temp != None:
            print(temp.val, end=' ')
            temp = temp.next
        print('')

class Solution:
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        head, temp = None, None
        temp_l1 = l1
        temp_l2 = l2

        if temp_l1 != None and temp_l2 != None:
            if temp_l1.val <= temp_l2.val:
                head = temp_l1
                temp_l1 = temp_l1.next
            else:
                head = temp_l2
                temp_l2 = temp_l2.next
            temp = head

        #temp.print()

        while temp_l1 != None and temp_l2 != None:
            if temp_l1.val <= temp_l2.val:
                temp.next = temp_l1
                temp_l1 = temp_l1.next
            else:
                temp.next = temp_l2
                temp_l2 = temp_l2.next

            temp = temp.next

        #head.print()

        if temp_l1 == None and temp_l2 != None:
            if head == None:
                head = temp_l2
            else:
                temp.next = temp_l2
        elif temp_l1 != None and temp_l2 == None:
            if head == None:
                head = temp_l1
            else:
                temp.next = temp_l1

        return head





if __name__ == '__main__':
    l1 = ListNode(1)
    l1.next = ListNode(2)
    l1.next.next = ListNode(4)

    l2 = ListNode(1)
    l2.next = ListNode(3)
    l2.next.next = ListNode(4)

    l1.print()
    l2.print()

    s = Solution()
    result = s.mergeTwoLists(l1, l2)
    if result:
        result.print()

    l1 = None
    l2 = None
    result = s.mergeTwoLists(l1, l2)
    if result:
        result.print()
    else:
        print(result)


    l1 = None
    l2 = ListNode(0)
    result = s.mergeTwoLists(l1, l2)
    if result:
        result.print()
