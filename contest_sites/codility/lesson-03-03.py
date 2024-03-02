#!/usr/bin/env python3
# Tape equilibrium

def solution_1(A):
    n = len(A)
    minimum_difference = sum(A)

    for i in range(1, n):
        print(A[:i])
        print(A[i:])
        subarray_1_total = sum(A[:i])
        subarray_2_total = sum(A[i:])
        difference = abs(subarray_1_total - subarray_2_total)
        print(difference)
        if difference < minimum_difference:
            minimum_difference = difference

    return minimum_difference



def solution(A):
    n = len(A)
    minimum_difference = sum(A)

    # 1st cut
    subarray_1_total = sum(A[:1])
    subarray_2_total = sum(A[1:])

    difference = subarray_1_total - subarray_2_total
    abs_minimum_difference = abs(difference)

    for i in range(1,n-1):
        difference = difference + 2 * A[i]
        abs_difference = abs(difference)

        if abs_difference < abs_minimum_difference:
            abs_minimum_difference = abs_difference

    return abs_minimum_difference


print(solution([3, 1, 2, 4, 3]))
