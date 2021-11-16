#!/usr/bin/env python3

from typing import *

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        m = 0
        def traverse(tn: TreeNode, level) -> int:
            if tn == None:
                return

            nonlocal m
            if level > m:
                m = level

            traverse(tn.left, level+1)
            traverse(tn.right, level+1)

        traverse(root, 1)
        return m


a = TreeNode(10)
a.left = TreeNode(5)
a.left.left = TreeNode(4)
a.left.left.left = TreeNode(2)
a.left.right = TreeNode(6)

a.right = TreeNode(5)
a.right.right = TreeNode(4)
a.right.left = TreeNode(1)
a.right.right.right = TreeNode(2)


s = Solution()
print(s.maxDepth(a))
