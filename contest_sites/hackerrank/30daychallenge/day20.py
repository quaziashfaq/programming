#!/usr/bin/python3

import sys

n = int(input().strip())
a = list(map(int, input().strip().split(' ')))

num_of_swaps = 0

i = 0
while i < n:
    #assuming the array is already sorted
    sorted = True

    j = 0
    while j < n - 1:
        if a[j] > a[j+1]:
            a[j], a[j+1] = a[j+1], a[j]
            num_of_swaps += 1
            sorted = False

        j += 1
    if sorted == True:
        break
    i += 1

print('Array is sorted in %d swaps.' % num_of_swaps)
print('First Element: %d' % a[0])
print('Last Element: %d' % a[-1])
