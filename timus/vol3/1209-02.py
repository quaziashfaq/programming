#!/usr/bin/env python3

def binary_search(a, key, start, end):

    #print("Start: {}, End: {}".format(start, end))
    if start > end:
        return -1

    while start <= end:
        mid = int((start+end) / 2)
        #print("Mid: {}".format(mid))
        if a[mid] == key:
            return mid
        elif a[mid] > key:
            #return binary_search(a, key, start, mid-1)
            end = mid - 1
        elif a[mid] < key:
            #return binary_search(a, key, mid+1, end)
            start = mid + 1
        else:
            return -1

    return -1



def generate_array(n):
    a = [0] * n
    a[0] = 1
    i = 1

    '''
    Here the sequence is 1, 10, 100, 1000, 10000, 100000, ...
    The length of each number is as follows: 1, 2, 3, 4, 5, 6, ...
    So the position of each 1 is as follows: 1, 2, 4, 7, 11, 16, 22
    Therefore we are adding the length of each number to the previous 1's positional value.
    a[0] = 1 --> this is the 1st one
    a[1] = a[0] + 1 = 2
    a[2] = a[1] + 2 = 4
    a[3] = a[2] + 3 = 7
    a[4] = a[3] + 4 = 11
    '''
    while i < n:
        a[i] = a[i-1] + i
        i += 1
    return a

#print(a)

def is_value_in_array(a, array_len, value):
    if binary_search(a, value, 0, array_len-1) == -1:
        return False
    else:
        return True

def main():
    output_string = ''
    array_len = 65536
    a = generate_array(array_len)
    n = int(input())
    for i in range(n):
        k = int(input())
        hasit = is_value_in_array(a, array_len, k)
        #print(hasit)
        if hasit == True:
            #print(1, end=' ')
            output_string += '1 '
        else:
            #print(0, end=' ')
            output_string += '0 '
    output_string.rstrip()
    print(output_string)

main()
