#!/usr/bin/env python3

line = input()
n, m = [int(i) for i in line.strip().split()]
m = m + 1
print(n*m)
