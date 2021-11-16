#!/usr/bin/env python3

from typing import *

# Tree problem
# Given the root of a binary tree, return the inorder traversal of its nodes' values.

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []

        def traverse(root):
            if root == None:
                return
            traverse(root.left)
            result.append(root.val)
            #print(result.val)
            traverse(root.right)

        traverse(root)
        return result

print('teest')
a = TreeNode(10)
a.left = TreeNode(5)
a.left.left = TreeNode(4)
a.left.right = TreeNode(6)
a.right = TreeNode(20)

s = Solution()
#assert s.inorderTraversal(a) == [4, 5, 6, 10, 20]
print(s.inorderTraversal(a))
#
