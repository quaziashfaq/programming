#!/usr/bin/env python3

def multiply(n, k):
    if n <= 0:
        return 1
    else:
        return n * multiply(n-k, k)

line = input()
n, k = line.split()
n = int(n)
k = len(k)

print(multiply(n,k))
