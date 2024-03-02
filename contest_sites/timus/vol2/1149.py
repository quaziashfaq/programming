#!/usr/bin/env pyhton3


def create_string(n):
    a = [0, 'sin(1']
    for i in range(2, n+1):
        if i % 2 == 0:
            a.append(a[i-1]+'-sin(' + str(i))
        else:
            a.append(a[i-1]+'+sin(' + str(i))

    for i in range(1, n+1):
        a[i] = a[i] + ')' * i

    #print(a)

    s = '(' * (n-1)
    for i in range(1, n):
        s += a[i] + '+' + str(n-i+1) + ')'

    s += a[n] + '+1'
    #print(s)
    return s


def main():
    n = int(input())
    print(create_string(n))


main()
