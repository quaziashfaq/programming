#!/usr/bin/env python3



def count_factorials(n):
    fvs = [0] * n
    fvs[0] = 1
    for i in range(1, n):
        fvs[i] = i * fvs[i-1]
    return fvs


def permute(npos, fvs, count_num):
    v = fvs[npos]
    for i in count_num.values():
        if i != 1:
            v = v // fvs[i]
    return v


def count_numbers(arr):
    c = {}
    for i in arr:
        if i not in c.keys():
            c[i] = 1
        else:
            c[i] += 1
    return c


def recur(tarr, arr, npos, cpos, n, fvs):
    '''
    npos = total number of positions in array
    cpos = current number of position in array
    so cpos < npos
    '''
    if cpos == npos:
        #print(arr, npos, cpos, n)
        total = sum(arr)
        c = count_numbers(arr)
        v = permute(npos, fvs, c)
        tarr[total] += v
        return

    for i in range(n, 10):
        barr_cpos = arr[cpos]
        arr[cpos] = i
        recur(tarr, arr, npos, cpos+1, i, fvs)
        arr[cpos] = barr_cpos


def main():
    n = int(input())
    half_n = n // 2
    array_size = half_n * 9 + 1
    arr = [0 for i in range(half_n)]
    tarr = [0 for i in range(array_size)]
    fvs = count_factorials(10)

    recur(tarr, arr, half_n, 0, 0, fvs)
    #print(tarr)
    #print(sum(tarr))
    ticket_count = [i*i for i in tarr]
    print(sum(ticket_count))


main()
