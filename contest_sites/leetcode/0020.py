#!/usr/bin/env python3

from typing import *



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
            return None
        return self.arr.pop(0)

    def stack_print(self):
        print(self.arr)

    def size(self):
        return len(self.arr)

class Solution:
    def isValid(self, s: str) -> bool:
        length = len(s)
        if length % 2 != 0:
            return False
        opening = '({['
        closing = ')}]'
        parantheses = {
            '(': ')',
            '{': '}',
            '[': ']'
        }

        stack = Stack()
        for i in s:
            if i in opening:
                stack.push(i)
            elif i in closing:
                ch = stack.pop()
                if ch == None:
                    return False
                if parantheses[ch] != i:
                    return False

        if stack.size() == 0:
            return True
        else:
            return False


if __name__ == '__main__':
    s = Solution()
    print(s.isValid("()"))      # True
    print(s.isValid("()[]{}"))  # True
    print(s.isValid("([)]"))    # False
    print(s.isValid("{[]}"))    # True
    print(s.isValid("(("))      # False
