#!/usr/bin/env python3

# Definition for a binary tree node.

from typing import *


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        maxpathsum = 0

        def traverse(node):
            nonlocal maxpathsum

            # I am returning -1 to offset the +1 in the below calculation
            # Because I am thinking that as I am going to left/right, there might
            # be a path. If there is no node at left/right, then I am returning -1
            # to offset my assumption (ie +1)

            if node == None:
                return -1
            lps = 1 + traverse(node.left)
            rps = 1 + traverse(node.right)


            inordersum = lps + rps
            maxpathsum = max(maxpathsum, inordersum, lps, rps)

            return max(lps, rps)

        traverse(root)
        return maxpathsum


if __name__ == '__main__':
    a = TreeNode(1)
    a.left = TreeNode(2)
    a.right = TreeNode(3)
    a.left.left = TreeNode(4)
    #a.left.right = TreeNode(5)
    a.left.left.left = TreeNode(6)
    #a.left.left.left.right = TreeNode(8)

    #a.left.right.left = TreeNode(7)
    #a.left.right.left.left = TreeNode(7)

    s = Solution()
    print(s.diameterOfBinaryTree(a))
