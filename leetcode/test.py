#!/usr/bin/env python3

from typing import *

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def add_a_node_to_left(tn: TreeNode, val):
    tn = TreeNode(val)

a = TreeNode(10)
print(a.val)
add_a_node_to_left(a.left, 5)

print(a.left.val)
