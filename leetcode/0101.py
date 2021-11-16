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
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:

        def traverse(left: TreeNode, right: TreeNode) -> bool:
            if left != None and right != None:
                print(left.val, right.val)
                if left.val == right.val:
                    result = traverse(left.left, right.right)
                    if result == True:
                        result = traverse(left.right, right.left)
                    return result
                else:
                    return False
            elif left == None and right == None:
                return True
            else:
                return False

        return traverse(root.left, root.right)


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
print(s.isSymmetric(a))
