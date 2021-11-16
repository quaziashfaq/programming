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
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head == None:
            return None
        if k == 1:
            return head
        pre = dummy_head = ListNode(0, head)

        def traverse(node, level, reverse=True):
            #print(node.val, level)
            if level == 1:
                return (reverse, node, node.next)
            else:
                #if node.next == None:
                if node == None or node.next == None:
                    reverse = False
                    return (reverse, None, None)
                else:
                    reverse, last_node_in_k, node_next_after_k = traverse(node.next, level-1)
                    if reverse == True:
                        node.next.next = node # Reversing
                        return (reverse, last_node_in_k, node_next_after_k)
                    else:
                        return (reverse, None, None)

        reverse, last_node_in_k, node_next_after_k = traverse(pre.next, k)
        while reverse == True:
            t = pre # Storing the previous node before group of k nodes
            pre = pre.next # jumping ahead and pointing to the last node in the new group of k nodes

            t.next = last_node_in_k # Now stiching the link back. after reversing, linking the t with previous last node in the group (or now 1st node)
            pre.next = node_next_after_k # In newly formed group, pre points to the last node and linking it with the 1st node after the group.

            reverse, last_node_in_k, node_next_after_k = traverse(pre.next, k)

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

    for k in range(1, 6):
        l1 = create_linked_list([1, 2, 3, 4, 5, 6])
        print_linked_list(l1)

        result = s.reverseKGroup(l1, k)
        if result:
            result.print()
            print('-'*50)
        delete_linked_list(l1)
