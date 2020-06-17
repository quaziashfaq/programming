#!/usr/bin/env python3


def solution(X, A):
    n = len (A)
    HIGH_SEC = n+1
    # position holds the seconds when leaf dropped for
    # a particular position.
    sec_needed_for_position = [HIGH_SEC] * (X+1)

    for each_second in range(n):
        if sec_needed_for_position[A[each_second]] > each_second:
            sec_needed_for_position[A[each_second]] = each_second
    print(sec_needed_for_position)

    # check if every position has a leaf.
    # Position started from 1 not 0 so the checking the array from [1:]
    max_sec_needed = 0
    for sec in sec_needed_for_position[1:]:
        if sec > max_sec_needed:
            max_sec_needed = sec

    if max_sec_needed == HIGH_SEC:
        return -1
    else:
        return max_sec_needed


print(solution(5, [1, 3, 1, 4, 2, 3, 5, 4]))
