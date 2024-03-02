#!/usr/bin/python3
# JUDGE_ID: 41750CH

import sys

def divide_by_d(n, d):
    count = 0
    r = n % d
    while r == 0 and n > 1:
        count += 1
        n = n // d
        r = n % d
    return (n, count)

def calculate(n):
    if n == 0:
        print(10)
    elif n >= 1 and n <= 9:
        print(n)
    else:
        count_of_divisions = [0 for i in range(10)]
        nn = n

        i = 9
        while i >= 2:
            nn, c = divide_by_d(nn, i)
            count_of_divisions[i] = c
            i -= 1

        if not nn == 1:
            print(-1)
        else:
            #v = 1
            number = ''
            for i in range(2, 10):
                number += str(i) * count_of_divisions[i]
                #v *= i ** count_of_divisions[i]
            print(number)
            # if v != n:
            #     print(v)
            #     print(n)
            #     sys.exit("Value not equal")



#for i in range(10**9+1):
#    print(i, ' : ', end ='')


n = int(input())
calculate(n)
