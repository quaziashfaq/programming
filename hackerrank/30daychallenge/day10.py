#!/usr/bin/python3


# Day 10: Binary Numbers


def find_longest_ones_in_binary(n):
    current_length = 0
    maximum_length = 0

    q = n // 2
    r = n % 2
    while not ((q==0) and (r==0)):
        if r == 1:
            current_length += 1
        elif r == 0:
            if maximum_length < current_length:
                maximum_length = current_length
            current_length = 0
        n = q
        q = n // 2
        r = n % 2


    if maximum_length < current_length:
        maximum_length = current_length

    return maximum_length

def test_data():
    for i in range(1, 20):
        s = '{:b}'.format(i)
        s = s + ' ' + str(find_longest_ones_in_binary(i))
        print(s)


if __name__ == '__main__':
    n = int(input())
    print(find_longest_ones_in_binary(n))
