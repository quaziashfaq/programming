#!/usr/bin/python3

# Day 16 : Exception

s = input().strip()

try:
    i = int(s)
    print(i)
except ValueError:
   print('Bad String')
