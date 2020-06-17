#!/usr/bin/env python3

class DataStructure:
    def __init__(self):
        self.data = []
    def __repr__(self):
        return '{!r}'.format(self.data)
    def push(self, v):
        self.data.append(v)

class Stack(DataStructure):
    '''
    LIFO = Last in, First out
    '''
    def pop(self):
        return self.data.pop()

class Queue(DataStructure):
    '''
    LIFO = Last in, First out
    '''
    def pop(self):
        return self.data.pop(0)


s = Stack()
s.push(10)
s.push(11)
s.push('\n')

print(s)
s.pop()
print(s)

print('-' * 80)
q = Queue()
q.push(11)
q.push(12)
q.push(13)
q.push(14)
print(q)
q.pop()
print(q)
