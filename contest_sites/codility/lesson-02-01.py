#!/usr/bin/env python3

def solution(A, K):
    if len(A) == 0:
        return A
    else:
        l = len(A)
        starting_position = 0

        # cut out the looping
        K = K % l

        starting_position = (l - K) % l
        newA = A[starting_position:] + A[0:starting_position]
        #print(newA)
        return newA

solution([3, 8, 9, 7, 6], 3)
solution([0,0,0], 1)
solution([1,2,3,4], 4)
print(solution([], 4))
