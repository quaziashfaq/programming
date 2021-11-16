#!/usr/bin/env python3

from typing import *

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        levels_dict = {}

        def traverse(tn: TreeNode, level: int):
            if tn == None:
                return
            if not level in levels_dict:
                levels_dict[level] = []
            levels_dict[level].append(tn.val)
            traverse(tn.left, level+1)
            traverse(tn.right, level+1)

        traverse(root, 0)
        result = []
        for i in sorted(levels_dict):
            result.append(levels_dict[i])

        return result


a = TreeNode(10)
a.left = TreeNode(5)
a.left.left = TreeNode(4)
a.left.right = TreeNode(6)
a.right = TreeNode(5)
a.right.left = TreeNode(4)
a.right.right = TreeNode(6)


s= Solution()
print(s.levelOrder(a))
