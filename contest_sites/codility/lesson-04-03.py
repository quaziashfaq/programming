#!/usr/bin/env python3

# MAX counter

def solution(N, A):
    counter = [0] * (N+1)
    last_max_value = 0
    next_max_value = 0

    for operation_number in A:
        if 1 <= operation_number <= N:
            if counter[operation_number] < last_max_value:
                counter[operation_number] = last_max_value
            counter[operation_number] += 1
            if counter[operation_number] > next_max_value:
                next_max_value = counter[operation_number]
        elif operation_number == N+1:
            last_max_value = next_max_value

    for i in range(len(counter)):
        if counter[i] < last_max_value:
            counter[i] = last_max_value
#    print(counter)
    return counter[1:]

assert(solution(5, [3, 4, 4, 6, 1, 4, 4]) == [3, 2, 2, 4, 2])
