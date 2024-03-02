#!/usr/bin/env python3
# Find the missing element

def solution_A(A):
    N = len(A)
    found = [False for i in range(0,N+2)]

    for i in A:
        found[i] = True

    for i in range(1, N+2):
        if found[i] == False:
            break
    return i


def solution(A):
    N = len(A)
    array_total = sum(A)
    would_be_total = (N+1) * (N+2) // 2
    missing_number = would_be_total - array_total
    return missing_number



print(solution([2, 5, 1, 3]))
