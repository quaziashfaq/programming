#!/usr/bin/env python3

a = [1, 2, 3, 4, 5]
print(sum(a[2:4]))
print(sum(a[3:6]))


def prefix_sums(a):
    n = len(a)
    p = [0] * (n+1)

    for i in range(len(a)):
        p[i+1] = p[i] + a[i]

    return p

p = prefix_sums(a)
print(p)

def count_total(p, x, y):
    return p[y+1] - p[x]

def count_total_with_boundary_check(p, x, y):
    if x < 0:
        x = 0
    l = len(p)
    if y > l - 2:
        y = l - 2
    return count_total(p, x, y)


print(count_total(p, 0, 2))
print(count_total(p, 1, 2))
print(count_total(p, 0, 4))

def mushrooms_1(A, k, m):
    p = prefix_sums(A)
    max_mushrooms_count = 0

    # going left first
    for i in range(m, -1, -1):
        left_position = k - i
        right_position = k
        cm = m
        cm -= 2 * i
        if cm > 0:
            right_position = k + cm
        mushrooms_count = count_total_with_boundary_check(p, left_position, right_position)
        if mushrooms_count > max_mushrooms_count:
            max_mushrooms_count = mushrooms_count

    # going right first
    for i in range(m, -1, -1):
        left_position = k
        right_position = k + i
        cm = m
        cm -= 2 * i
        if cm > 0:
            left_position = k - cm
        mushrooms_count = count_total_with_boundary_check(p, left_position, right_position)
        if mushrooms_count > max_mushrooms_count:
            max_mushrooms_count = mushrooms_count


    return max_mushrooms_count



def mushrooms(A, k, m):
    n = len(A)
    p = prefix_sums(A)
    max_mushrooms_count = 0
    mushrooms_picked = 0

    # going left first
    for i in range(min(m, k) + 1):
        left_position = k - i
        right_position = min(n-1, max(k, k+(m-2*i)))
        mushrooms_picked = max(mushrooms_picked, count_total(p, left_position, right_position))

    # going right first
    for i in range(min(m+1, n-k)):
        left_position = max(0, min(k, k-(m-2*i)))
        right_position = k + i
        mushrooms_picked = max(mushrooms_picked, count_total(p, left_position, right_position))

    return mushrooms_picked


print(mushrooms([2, 3, 7, 5, 1, 3, 9], 4, 6))
