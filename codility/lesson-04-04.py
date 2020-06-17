#!/usr/bin/env python3

def solution(A):

    print(A)
    B = [i for i in A if i > 0]
    if B == []:
        return 1

    print(B)
    B = list(set(B))
    print(B)
    B.sort()
    B = [0] + B
    print(B)

    for i in range(1, len(B)):
        print(i)
        if B[i] != i:
            return i
    return i+1


print(solution([-2, -1, -10]))
print(solution([10, -10, 120]))
print(solution([1, 3, 6, 4, 1, 2]))
print(solution([1,2,3]))
