#!/usr/bin/env python3

from typing import *

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def print(self):
        t = self
        while t != None:
            print(t.val, end=' ')
            t = t.next
        print('')

class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None:
            return None
        pre = dummy_head = ListNode(0, head)
        t1 = head
        t2 = t1.next
        while t2 != None:
            #print(pre.val, t1.val, t2.val)
            pre.next = t2
            t1.next = t2.next
            t2.next = t1

            pre = t1
            t1 = t1.next
            if t1 != None:
                t2 = t1.next
            else:
                t2 = None

        return dummy_head.next



if __name__ == '__main__':
    def create_linked_list(l):
        head =  ListNode(l[0])
        t = head
        for i in range(1, len(l)):
            t.next = ListNode(l[i])
            t = t.next

        return head

    def delete_linked_list(node):
        t = node
        while t != None:
            node = node.next
            del t
            t = node

    def print_linked_list(node):
        t = node
        while t != None:
            print(t.val, end=' ')
            t = t.next
        print('')



    l1 = create_linked_list([1, 2, 3, 4, 5])
    l1.print()

    s = Solution()
    result = s.swapPairs(l1)
    if result:
        result.print()

    print('-'*50)
    l2 = create_linked_list([1, 2, 3, 4])
    l2.print()
    result = s.swapPairs(l2)
    if result:
        result.print()

    print('-'*50)
    l2 = create_linked_list([1])
    l2.print()
    result = s.swapPairs(l2)
    if result:
        result.print()

    print('-'*50)
    result = s.swapPairs(None)
    if result:
        result.print()
