#!/usr/bin/env python3
#
from typing import *

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        t1 = l1
        t2 = l2

        r = ListNode()
        t = r
        c = 0 # carry forward
        s = 0 # sum
        while True:
            s = c + t1.val + t2.val # sum
            c = s // 10 # carry forward
            t.val = s % 10
            #print(t1.val, t2.val, t.val, c)
            t1 = t1.next
            t2 = t2.next
            if t1 != None and t2 != None:
                t.next = ListNode()
                t = t.next
            else:
                break

        while t1 != None:
            s = c + t1.val
            t.next = ListNode(s % 10)
            t = t.next
            t1 = t1.next
            c = s // 10


        while t2 != None:
            s = c + t2.val
            t.next = ListNode(s % 10)
            t = t.next
            t2 = t2.next
            c = s // 10

        if c > 0:
            t.next = ListNode(c)

        return r
         


if __name__ == '__main__':
    s = Solution()

    def create_linked_list(l):
        head =  ListNode(l[0])
        temp = head
        for i in range(1, len(l)):
            temp.next = ListNode(l[i])
            temp = temp.next

        return head

    def delete_linked_list(node):
        temp = node
        while temp != None:
            node = node.next
            del temp
            temp = node

    def print_linked_list(node):
        temp = node
        while temp != None:
            print(temp.val, end=' ')
            temp = temp.next
        print('')


    num1 = create_linked_list([9, 9, 9, 9, 9, 9])
    num2 = create_linked_list([1])
    print_linked_list(num1)
    print_linked_list(num2)
    print('-' * 60)
    result = s.addTwoNumbers(num1, num2)
    print_linked_list(result)
    print('-' * 60)
