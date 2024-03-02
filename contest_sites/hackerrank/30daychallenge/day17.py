#!/usr/bin/python3

class Calculator:
    def __init__(self):
        pass

    def power(self, n, p):
        if n < 0 or p < 0:
            raise Exception('n and p should be non-negative')
        return n ** p


n = int(input())
for i in range(n):
    line = input()
    n,p = [int(i) for i in line.strip().split()]
    c = Calculator()
    try:
        result = c.power(n, p)
        print(result)
    except Exception as e:
        print(e)
