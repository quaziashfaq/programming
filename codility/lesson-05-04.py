#!/usr/bin/env python3

def solution(A, B, K):
    n1 = B // K
    n2 = (A-1) // K
    n = n1 - n2
    return n

print(solution(6, 11, 2))
print(solution(11, 345, 17))
print(solution(11, 11, 17))
print(solution(0, 0, 17))
print(solution(0, 2000000000, 2000000000))
