#!/usr/bin/env python3

from typing import *

# Tree problem

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        balanced = True

        def postOrderTraversal(tn: TreeNode) -> int:
            nonlocal balanced

            if tn == None:
                return 0

            leftSubTreeDepth = postOrderTraversal(tn.left)
            rightSubTreeDepth = postOrderTraversal(tn.right)

            if abs(leftSubTreeDepth - rightSubTreeDepth) > 1:
                balanced = False

            return max(leftSubTreeDepth, rightSubTreeDepth)+1

        postOrderTraversal(root)
        return balanced


        
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


a = TreeNode(3)
a.left = TreeNode(9)
a.right = TreeNode(20)
a.right.left = TreeNode(15)
a.right.right = TreeNode(7)
a.right.right.right = TreeNode(8)

s = Solution()
print(s.inorderTraversal(a))
print(s.isBalanced(a))
