#!/usr/bin/env python3

n = int(input())
groups = [int(x) for x in input().split()]

half = n // 2 + 1
groups.sort()

total = 0
for i in range(half):
    total += groups[i] // 2 + 1

print(total)
