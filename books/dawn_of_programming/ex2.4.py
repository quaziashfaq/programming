#!/usr/bin/env python3

# 1 + 2 + 3 + ... + n
n = 10
total = 0
i = 1
while i <= n:
    total += i
    i += 1
print(total)

# 1^2 + 2^2 + 3^2 + ... + n^2
n = 10
total = 0
i = 1
while i <= n:
    total += i * i
    i += 1
print(total)

# 1^1 + 2^2 + 3^3 + ... + n^n
n = 10
total = 0
i = 1
while i <= n:
    total += i ** i
    i += 1
print(total)

# 1 + (2 + 3) + (4 + 5 + 6) + ... + n-th term
n = 3
total = 0
i = 1
j = 1
while i <= n:
    k = 1
    while k <= i:
        print(j)
        total += j
        j += 1
        k += 1
    i += 1
print(total)


# 1 + (2 + 3*4) + (5 + 6*7 + 8*9*10) + ... + n-th term
n = 4
total = 0
i = 1
j = 1
print('i', 'k', 'l', 'j')
while i <= n:
    k = 1
    t1 = 0
    while k <= i:
        l = 1
        t2 = 1
        while l <= k:
            print(i, k, l, j)
            t2 *= j
            l += 1
            j += 1
        t1 += t2
        k += 1
    total += t1
    i += 1

print(total)


n = 3
i = 1
total = 0
while i <= n:
    total += i * (n-i+1)
    i += 1
print(total)



n = 10
i = 1
j = n - i
while i <= n:
    k = 1
    while k <= i:
        print('*', end='')
        k += 1
    k = 1
    while k <= j:
        print('.', end='')
        k += 1
    i += 1
    j = n - i
    print('')

n = 3
i = n
j = n - i
while i >= 1:
    k = 1
    while k <= j:
        print('.', end='')
        k += 1
    k = 1
    while k <= i:
        print('*', end='')
        k += 1
    i -= 1
    j = n - i
    print('')



print('-' * 80)
n = 6
i = 1
while i <= n:
    no_dots = n - i
    no_stars = i * 2 - 1
    print('.' * no_dots, end='')
    print('*' * no_stars, end ='')
    print('.' * no_dots, end='')
    i += 1
    print('')



print('-' * 80)
n = 3
i = n
while i >= 1:
    no_dots = n - i
    print('.' * no_dots, end='')
    j = 1
    while j < i:
        print(j, end='')
        j += 1
    print(i, end='')
    j = 1
    while j < i:
        print(j, end='')
        j += 1
    print('.' * no_dots, end='')
    i -= 1
    print('')



# Diamond
print('-' * 80)
n = 6
i = 1
while i <= n:
    no_dots = n - i
    no_stars = i * 2 - 1
    print('.' * no_dots, end='')
    print('*' * no_stars, end ='')
    print('.' * no_dots, end='')
    i += 1
    print('')

i = n - 1
while i >= 1:
    no_dots = n - i
    no_stars = i * 2 - 1
    print('.' * no_dots, end='')
    print('*' * no_stars, end ='')
    print('.' * no_dots, end='')
    i -= 1
    print('')




print('-' * 80)
n = 6
i = 1
while i <= n:
    no_dots = n - i
    print('.' * no_dots, end='')
    j = 1
    while j < i:
        print(j, end='')
        j += 1
    print(i, end='')
    j = 1
    while j < i:
        print(j, end='')
        j += 1
    print('.' * no_dots, end='')
    i += 1
    print('')

i = n - 1
while i >= 1:
    no_dots = n - i
    print('.' * no_dots, end='')
    j = 1
    while j < i:
        print(j, end='')
        j += 1
    print(i, end='')
    j = 1
    while j < i:
        print(j, end='')
        j += 1
    print('.' * no_dots, end='')
    i -= 1
    print('')
