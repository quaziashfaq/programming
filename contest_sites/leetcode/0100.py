#!/usr/bin/env python3
#
#
from typing import *

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

        def traverse(pTree: TreeNode, qTree: TreeNode) -> bool:
            if pTree != None and qTree != None:
               if pTree.val != qTree.val:
                   return False
               result = traverse(pTree.left, qTree.left)
               if result == True:
                    result = traverse(pTree.right, qTree.right)
               return result
            elif pTree == None and qTree == None:
                return True
            else:
                return False

        return traverse(p, q)

a = TreeNode(10)
a.left = TreeNode(5)
a.left.left = TreeNode(4)
a.left.right = TreeNode(6)
a.right = TreeNode(20)

b = TreeNode(10)
b.left = TreeNode(5)
b.left.left = TreeNode(4)
b.left.right = TreeNode(6)
b.right = TreeNode(20)

s = Solution()
print(s.isSameTree(a, b))
