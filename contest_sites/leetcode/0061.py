#!/usr/bin/env python3

from typing import *

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head == None:
            return None
        if k == 0:
            return head
        n = 1
        t = head
        while t.next != None:
            n += 1
            t = t.next
        last_node = t

        k = k % n
        if k == 0:
            return head
        else:
            i = 1
            # calculating how many nodes I need to pass to get to the right location
            # so that the rest of the nodes will come to the beginning of the list.
            # [1, 2, 3, 4, 5], 2 => [4, 5, 1, 2, 3]
            # so k = 2
            # k = n - k = 3 => The last 2 nodes will come to the front of first 3 nodes.
            k = n - k
            t = head
            while i != k:
                i += 1
                t = t.next

            # Now stitching it back.
            # t is pointing to node 3.
            new_head = t.next
            t.next = None
            last_node.next = head

            return new_head





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

    for k in range(1, 7):
        l1 = create_linked_list([1, 2, 3, 4, 5, 6])
        print_linked_list(l1)

        result = s.rotateRight(l1, k)
        if result:
            print_linked_list(result)
            print('-'*50)
        delete_linked_list(l1)
