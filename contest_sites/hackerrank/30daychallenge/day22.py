#!/usr/bin/python3

class Node:
    def __init__(self,data):
        self.right=self.left=None
        self.data = data

class Solution:
    def insert(self,root,data):
        if root==None:
            return Node(data)
        else:
            if data<=root.data:
                cur=self.insert(root.left,data)
                root.left=cur
            else:
                cur=self.insert(root.right,data)
                root.right=cur
        return root

    def getHeight(self, root):
        left_hand_height = 0
        right_hand_height = 0

        if root == None:
            return -1
        else:
            print(root.data)
            left_hand_height = self.getHeight(root.left)
            right_hand_height = self.getHeight(root.right)

            return (max(left_hand_height, right_hand_height) + 1)


T = int(input())
myTree = Solution()
root = None
for i in range(T):
    data = int(input())
    root = myTree.insert(root,data)
height = myTree.getHeight(root)
print(height)
