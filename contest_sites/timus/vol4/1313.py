#!/usr/bin/env python3

def main():
    n = int(input())
    monitor = []
    for i in range(n):
        line = [int(i) for i in input().split()]
        monitor.append(line)
    #print(monitor)

    new_monitor = []

    for i in range(n):
        j = i
        k = 0
        while j >= 0:
            new_monitor.append(monitor[j][k])
            j = j - 1
            k = k + 1

    for i in range(1, n):
        j = n - 1
        k = i
        while k <= n-1:
            new_monitor.append(monitor[j][k])
            j = j - 1
            k = k + 1

    for i in new_monitor:
        print(i, end=' ')

    print('')


main()
