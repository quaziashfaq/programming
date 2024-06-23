#!/usr/bin/env python3

ordinal_numbers = []
for i in range(1, 10):
    if i == 1:
        msg = '1st'
    elif i == 2:
        msg = '2nd'
    elif i == 3:
        msg = '3rd'
    else:
        msg = f'{i}th'

    ordinal_numbers.append(msg)

print(' '.join(ordinal_numbers))
