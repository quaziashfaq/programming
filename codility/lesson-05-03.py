#!/usr/bin/env python3

def solution(A):
    n = len(A)
    minimal_average = sum(A) / n
    pos_minimal_average = 1

    count = [0 for i in range(n)]
    total = [0 for i in range(n)]
    average = [minimal_average for i in range(n)]

    # count the prefix averages and fining the minimal average
    count[0] = 1
    total[0] = A[0]
    for i in range(1, n):
        # continue from the previous minimal average
        c1 = count[i-1] + 1
        t1 = total[i-1] + A[i]
        a1 = t1 / c1

        # or calculate average of the previous value and current value
        c2 = 2
        t2 = A[i-1] + A[i]
        a2 = t2 / c2

        # then compare and store the minimum result
        if a1 <= a2:
            count[i] = c1
            total[i] = t1
            average[i] = a1
        else:
            count[i] = c2
            total[i] = t2
            average[i] = a2

        if minimal_average <= average[i]:
            pass
        else:
            minimal_average = average[i]
            pos_minimal_average = i


    starting_position = pos_minimal_average - count[pos_minimal_average] + 1
    return starting_position



print(solution([2, 2, 3]))
print(solution([4, 2, 2, 5, 1, 5, 8]))
print(solution([4, 5, 4, 5, 1, 5, 8]))
