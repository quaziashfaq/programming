#!/usr/bin/env python3

# Definition for a binary tree node.

from typing import *


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        maxpathsum = root.val

        def traverse(node):
            nonlocal maxpathsum

            if node == None:
                return 0
            lps = traverse(node.left)
            rps = traverse(node.right)

            inordersum = node.val + lps + rps
            leftpathsum = node.val + lps
            rightpathsum = node.val + rps

            maxpathsum = max(maxpathsum, node.val, inordersum, leftpathsum, rightpathsum)

            return max(node.val, leftpathsum, rightpathsum)

        traverse(root)
        return maxpathsum


if __name__ == '__main__':
    a = TreeNode(-10)
    a.left = TreeNode(-9)
    a.right = TreeNode(20)
    a.right.left = TreeNode(15)
    a.right.right = TreeNode(7)

    s = Solution()
    print(s.maxPathSum(a))

    a = TreeNode(9)
    a.left = TreeNode(6)
    a.right = TreeNode(-3)
    a.right.left = TreeNode(-6)
    a.right.right = TreeNode(2)
    a.right.right.left = TreeNode(2)
    a.right.right.left.left = TreeNode(-6)
    a.right.right.left.right = TreeNode(-6)
    a.right.right.left.left.left = TreeNode(-6)

    print(s.maxPathSum(a))
