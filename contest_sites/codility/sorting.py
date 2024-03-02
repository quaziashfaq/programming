#!/usr/bin/env python3

def selection_sort(arr):
    print(arr)
    n = len(arr)
    for i in range(n):
        minval = arr[i]
        minval_pos = i
        for j in range(i+1, n):
            if minval > arr[j]:
                minval = arr[j]
                minval_pos = j
        arr[i], arr[minval_pos] = arr[minval_pos], arr[i]
        print(arr)

    return arr


def bubble_sort(arr):
    print(arr)
    n = len(arr)
    for i in range(n):
        minval = arr[i]
        minval_pos = i
        for j in range(i+1, n):
            if minval > arr[j]:
                minval = arr[j]
                minval_pos = j
        arr[i], arr[minval_pos] = arr[minval_pos], arr[i]
        print(arr)

    return arr



a = [5, 2, 8, 16, 1, 14]
print(selection_sort(a))
