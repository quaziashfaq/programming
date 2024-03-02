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
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        tn = None

        def buildBST(left: int, right: int, nums: List[int]) -> TreeNode:
            if left > right:
                return None
            elif left == right:
                tn = TreeNode(nums[left])
            else:
                mid = (left + right) // 2
                tn = TreeNode(nums[mid])
                tn.left = buildBST(left, mid-1, nums)
                tn.right = buildBST(mid+1, right, nums)
            return tn

        tn = buildBST(0, len(nums)-1, nums)
        return tn

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


nums = [ -10, -3, 0, 5, 9]
s = Solution()
rootNode = s.sortedArrayToBST(nums)
r = s.inorderTraversal(rootNode)
print(r)
