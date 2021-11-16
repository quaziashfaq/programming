#!/usr/bin/env python3

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


null = 0


class Stack:
    def __init__(self):
        self.arr = []

    def push(self, val: int):
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
        self.root = root
        self.is_left_traversed = [False for i in range(len(root))]
        self.is_traversed = [False for i in range(len(root))]
        self.right_traversed = [False for i in range(len(root))]
        self.stack = Stack()
        self.stack.push(0)

    def hasLeftNode(self, index):
        left = index * 2 + 1
        return left < len(self.root) and self.root[left] != null

    def hasRightNode(self, index):
        right = index * 2 + 2
        return right < len(self.root) and self.root[right] != null


    def next(self) -> int:
        i = self.stack.pop()

        while not self.is_traversed[i]:
            while self.hasLeftNode(i) and not self.is_left_traversed[i]:
                self.is_left_traversed[i] = True
                self.stack.push(i)
                i = i * 2 + 1

            if not self.is_traversed[i]:
                self.is_traversed[i] = True

            if self.hasRightNode(i):
                right = i * 2 + 2
                self.stack.push(right)

        return self.root[i]


    def hasNext(self) -> bool:
        return self.stack.size() > 0


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()
#
bi = BSTIterator([7, 3, 15, 1, null, 9, 20])

print(bi.next())    #// return 1
bi.stack.stack_print()
print(bi.next())    #// return 3
bi.stack.stack_print()
print(bi.next())    #// return 7
bi.stack.stack_print()

print(bi.hasNext())
print(bi.next())    #// return 9
bi.stack.stack_print()
print(bi.next())    #// return 15
bi.stack.stack_print()
print(bi.next())    #// return 20
print(bi.hasNext())
bi.stack.stack_print()
