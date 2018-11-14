#!/usr/bin/env python3

import sys

def calculate_cycle_length(cycle_length, n, cycle_length_dictionary, v):
    if v == 1:
        return 1

    if v % 2 == 0:
        next_value = int(v / 2)
    else:
        next_value = int(3 * v + 1)

    if v < n:
        if cycle_length[v] == 0:
            cycle_length[v] = 1 + calculate_cycle_length(cycle_length, n, cycle_length_dictionary, next_value)
        return cycle_length[v]

    else:
        if v not in cycle_length_dictionary.keys():
            cycle_length_dictionary[v] = 1 + calculate_cycle_length(cycle_length, n, cycle_length_dictionary, next_value)
        return cycle_length_dictionary[v]

def generate_array(n):
    n2 = 3 * n
    cycle_length = [0] * n2
    cycle_length_dictionary = {} # For values greater than (1,000,000 - 1)

    cycle_length[1] = 1
    for i in range(2, n):
        cycle_length[i] = calculate_cycle_length(cycle_length, n2, cycle_length_dictionary, i)

    return (cycle_length, cycle_length_dictionary)


def main():
    cl, cld = generate_array(1000000)

    lines = sys.stdin.readlines()
    for line in lines:
        a, b = list(map(int, line.split()))
        if a > b:
            aa, bb = b, a
        else:
            aa, bb = a, b

        m = max(cl[aa:(bb+1)])
        print(a, b, m)


if __name__=="__main__":
    main()
