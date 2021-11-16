#!/usr/bin/env python3
#
from typing import *

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        def traverse(prenode, node, n=n):
            nonlocal head
            if node == None:
                return 1
            i = traverse(node, node.next)
            if i == n:
                print(i, node.val)
                if node == head:
                    head = head.next
                else:
                    prenode.next = node.next
            return i + 1

        traverse(None, head, n)
        return head



if __name__ == '__main__':
    s = Solution()

    def create_linked_list():
        ln = ListNode(1)
        ln.next = ListNode(2)
        ln.next.next = ListNode(3)
        ln.next.next.next = ListNode(4)
        ln.next.next.next.next = ListNode(5)
        return ln

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


    for i in range(5,0, -1):
        print(i)
        ln = create_linked_list()
        print_linked_list(ln)
        ln = s.removeNthFromEnd(ln, i)
        print_linked_list(ln)
        print('-' * 60)
        delete_linked_list(ln)
