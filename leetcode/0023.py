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
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if lists == None:
            return None
        head = None
        for l in lists:
            head = self.mergeTwoLists(head, l)
            if head:
                head.print()

        return head

    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        head, t = None, None
        t1 = l1
        t2 = l2

        if t1 != None and t2 != None:
            if t1.val <= t2.val:
                head = t1
                t1 = t1.next
            else:
                head = t2
                t2 = t2.next
            t = head

        #t.print()

        while t1 != None and t2 != None:
            if t1.val <= t2.val:
                t.next = t1
                t1 = t1.next
            else:
                t.next = t2
                t2 = t2.next

            t = t.next

        if t1 == None and t2 != None:
            if head == None:
                head = t2
            else:
                t.next = t2
        elif t1 != None and t2 == None:
            if head == None:
                head = t1
            else:
                t.next = t1

        return head





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



    l1 = create_linked_list([1, 4, 5])
    l2 = create_linked_list([1, 3, 4])
    l3 = create_linked_list([2, 6])
    l1.print()
    l2.print()
    l3.print()

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


    print('-' * 50)
    l1 = create_linked_list([1, 4, 5])
    l2 = create_linked_list([1, 3, 4])
    l3 = create_linked_list([2, 6])
    result = s.mergeKLists([l1, l2, l3])
    if result:
        result.print()

    l1 = None
    result = s.mergeKLists([None])
    if result:
        result.print()
