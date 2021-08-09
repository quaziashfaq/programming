#!/usr/bin/python3

import sys

phoneBook = {}

n = int(input())
for i in range(0, n):
    s = input().rstrip().split()
    phoneBook[s[0]] = s[1]

#print(phoneBook)

for line in sys.stdin:
    name = line.strip()
    if name in phoneBook.keys():
        print('{}={}'.format(name, phoneBook[name]))
    else:
        print('Not found')
