#!/usr/bin/env python3

def print_shelf(m):
    for i in m:
        for j in i:
            print(j, end=' ')
        print('')

def main():
    n = int(input())
    shelf = []
    for i in range(n):
        shelf.append([0 for i in range(n)])
    #print_shelf(shelf)

    count = 1
    for i in range(n-1, -1, -1): # i is column number
        j = i # so j is column number
        k = 0 # k is row number
        while j < n:
            shelf[k][j] = count
            j = j + 1
            k = k + 1
            count = count + 1
    #print_shelf(shelf)

    for i in range(1, n): # i is row now
        j = i
        k = 0
        while j < n:
            shelf[j][k] = count
            j = j + 1
            k = k + 1
            count = count + 1
    print_shelf(shelf)
  
main()
