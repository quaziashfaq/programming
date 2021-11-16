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
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None:
            return None
        pre = dummy_head = ListNode(-101, head)

        t = head
        while t != None:
            duplicate_found = False
            while True:
                if t.next:
                    if t.val == t.next.val:
                        duplicate_found = True
                        print(t.val, t.next.val)
                        t = t.next
                    else:
                        break
                else:
                    break
            if duplicate_found:
                dummy_head.print()
                pre.next = t.next
            else:
                pre = t
            t = t.next

        print('Before returning: ', end=' ')
        dummy_head.print()
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



    s = Solution()

    l1 = create_linked_list([1])
    print_linked_list(l1)
    result = s.deleteDuplicates(l1)
    if result:
        print_linked_list(result)
    else:
        print('None')
    #delete_linked_list(l1)

    print('-' * 50)

    l1 = create_linked_list([1, 1, 1])
    print_linked_list(l1)
    result = s.deleteDuplicates(l1)
    if result:
        print_linked_list(result)
    else:
        print('None')
    #delete_linked_list(l1)
