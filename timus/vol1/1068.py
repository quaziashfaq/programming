#!/usr/bin/env python3

# Timus 1068

def sum_of_first_n_integers(n):
    return int(n * (n+1) / 2)


def find_sum(n):
    if n == 0:
        return 1
    elif n > 0:
        return sum_of_first_n_integers(n)
    elif n < 0:
        return 1 - sum_of_first_n_integers(-n)
    else:
        print('Error: I am not to be printed!!!')

n = int(input())
print(find_sum(n))
