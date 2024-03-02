#!/usr/bin/env python3

from typing import *

# Constraints:

# The number of nodes in the tree is in the range [1, 10^5].
# 0 <= Node.val <= 10^6
# At most 10^5 calls will be made to hasNext, and next.

# That's why I took null to be -1
null = -1

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        #print("Creating treen node. val: ", val)
        self.val = val
        self.left = left
        self.right = right

    def insert(self, val):
        #
        # Here we are using value of the 'val' to find the ultimate position of 'val'
        # in the big scheme of Tree.
        #

        temp = self # This is actually starting from root everytime
        while True:
            # if val is less than temp.val and if there is a left node of temp,
            #   then go further to your left
            #   Otherwise this temp.left is the position to place val.
            if val < temp.val:
                if temp.left != None:
                    temp = temp.left
                else:
                    temp.left = TreeNode(val)
                    return
            # if val is greater than temp.val and if there is a right node of temp,
            #   then go further to your right
            #   Otherwise this temp.right is the position to place val.
            elif val > temp.val:
                if temp.right != None:
                    temp = temp.right
                else:
                    temp.right = TreeNode(val)
                    return
            else:
                # I just presumed that there won't be any equal value.
                # All the values in the BST is unique
                # I will just ignore them if any duplicate value comes
                return

    # def __repr__(self):
    #     return self.val

    def traverse(self):
        # Traverse in-order. It will give ascending sorted list
        if self.left != None:
            self.left.traverse()
        print(self.val, end= ' ')
        if self.right != None:
            self.right.traverse()


class Stack:
    def __init__(self):
        # This is very generic Array. Literally you can push anything you like.
        # I think this is the beauty of Python. It's very easy to use and write code.
        # You can push an integer or a tuple (which I did in BSTIterator class! :-))
        # The challenge is there is no enforcing what I am pushing.
        # I have to mantain the consistency outside of the class.
        self.arr = []

    def push(self, val):
        self.arr.insert(0, val)

    def pop(self):
        if self.arr == []:
            return []
        return self.arr.pop(0)

    def stack_print(self):
        print(self.arr)

    def size(self):
        return len(self.arr)

class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        if isinstance(root, list):
            # If root is an array
            self.arr = root
            #print("Creating Tree Node")

            # Creating the whole BST
            self.root = TreeNode(self.arr[0])
            for i in range(1, len(self.arr)):
                if self.arr[i] != null:
                    self.root.insert(self.arr[i])
        else:
            # If root is a TreeNode
            self.root = root

        self.stack = Stack()
        # Pushed the root TreeNode.
        self.stack.push((self.root, False, False)) # Node, self_traversed, left_traversed
        # I haven't traversed it and its left yet.


    def next(self) -> int:
        n, traversed, leftTraversed = self.stack.pop()

        while not traversed:
            while n.left != None and not leftTraversed:
                # I haven't traversed the node yet. But I want to know if there is any nodes to its left.
                # Then go further down to the letf hand/leg/rabbit hole.
                # and push all of the nodes to the stack.
                # Once I get to the end leaf node and there is no node.left and I break out of while loop.
                leftTraversed = True
                self.stack.push((n, traversed, leftTraversed))
                n = n.left
                leftTraversed = False

            # I have traversed it. So I make the status True to get out of the upper while loop.
            if not traversed:
                traversed = True

            # Before leaving while loop, I just check if I have a righ node
            # then I push it into the stack.
            if n.right != None:
                self.stack.push((n.right, False, False))

        return n.val



    def hasNext(self) -> bool:
        # If there something in the stack, that means I have something left in the BST
        return self.stack.size() > 0



# Here I am testing my TreeNode class
# root = TreeNode(7)
# root.traverse()
# print()
# root.insert(3)
# root.traverse()
# print()
# root.insert(15)
# root.traverse()
# print()
# root.insert(1)
# root.traverse()
# print()
# root.insert(4)
# root.traverse()
# print()
# root.insert(20)
# root.traverse()
# print()
# root.insert(9)
# root.traverse()
# print()


# Here I am testing my BSTIterator class
bi = BSTIterator([7, 3, 15, 1, null, 9, 20])
print(bi.next())    #// return 1
print(bi.next())    #// return 3
print(bi.next())    #// return 7

print(bi.hasNext())
print(bi.next())    #// return 9
print(bi.next())    #// return 15
print(bi.next())    #// return 20
print(bi.hasNext())

