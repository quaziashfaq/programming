#!/usr/bin/env python3

n = 200000
primes = [0,]
p = [True] * n
p[0] = False
p[1] = False

for i in range (2, n):
    for j in range(2*i, n, i):
        p[j] = False

count = 0
for i in range(n):
    if p[i] == True:
        count += 1
        primes.append(i)

k = int(input())
for i in range(k):
    number = int(input())
    print(primes[number])
