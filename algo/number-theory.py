#!/usr/bin/env python3

import math

def is_it_leap_year(year):
    return year % 400 == 0 or (year % 100 != 0 and year % 4 == 0)

def get_primes(n):
    p = [True for i in range(n+1)]
    p[0] = p[1] = False

    primes = []
    for i in range(2, n+1):
        if p[i] == True: # First time, so it's a prime
            primes.append(i)
            for j in range(i*i, n+1, i):
                p[j] = False
    return primes


def factorize(n):
    factors = {}
    primes = get_primes(int(math.sqrt(n)))
    i = 0
    while i < len(primes) and n > 1:
        p = primes[i]
        while n % p == 0:         # as long as p can divide n
            if p not in factors:  # if p can divide for the first time then
                factors[p] = 1
            else:
                factors[p] += 1   # if p previously divides n
            n = n // p
        i += 1
    if n > 1:
        factors[n] = 1
    return factors

def get_number_of_divisors(n):
    f = factorize(n)
    total = 1
    for v in f.values():
        total *= (v+1) # if there are m terms of p in n, then to count number of divisors we can take 0, 1, ..., m number of p's. That's why (v+1)
    return total

def get_sum_of_divisors(n):
    f = factorize(n)
    total = 1
    for i in f:
        total *= (i ** (f[i] + 1) - 1) / (i -1)
    return int(total)

def gcd1(a, b):
    c = a % b
    if c == 0:
        return b
    else:
        return gcd(b, c)

def gcd(a, b):
    c = a % b
    while c != 0:
        a = b
        b = c
        c = a % b
    return b

def egcd(a, b):
    q = a // b
    r = a % b
    if r == 0:
        return (b, 0, 1)
    else:
        g, x, y = egcd(b, r)
        x1 = y
        y1 = -q * y + x
        return (g, x1, y1)

def lcd(a, b):
    g = gcd(a, b)
    l = a // g * b
    return l

def get_phi(n):
    f = factorize(n)
    phi = n
    for i in f:
        phi = phi // i * (i-1)
    return phi


def bigmod(base, power, M, level=0):
    #print("power={}\tlevel={}".format(power, level))
    if power == 0:
        return 1 % M
    elif power % 2 == 0:
        return (bigmod(base, power//2, M, level+1) ** 2) % M
    else:
        return (bigmod(base, power-1, M, level+1) * base) % M

def isodd(n):
    return n % 2 == 1

def iseven(n):
    return not isodd(n)



def bigsum(base, power, M, level=0):
    '''
    find 1 + a + a^2 + a^3 + a^4 + ... + a^(b-1)
    b is equal to power
    '''
    print('level = {}  power={}'.format(level, power))
    if power-1 == 0:
        return 1 % M
    elif iseven(power) == True: # even number of terms
        half_power = power // 2
        m1 = bigsum(base, half_power, M, level+1)
        m2 = (bigmod(base, half_power, M, level+1) * (m1 % M)) % M
        return (m1 + m2) % M
    else: # there are odd number of terms
        return (1 + (a % M) * bigsum(base, power-1, M, level+1)) % M


def bigsum1(base, b, M, level=0):
    '''
    find 1 + 2a + 3a^2 + 4a^3 + 5a^4 + ... + ba^(b-1)
    b is equal to power
    '''
    total = 1
    coeff = 1
    term = 1
    for i in range(1, b):
        coeff = i + 1
        term = (term * base) % M
        total = (total + coeff * term) % M
        print('coeff={}, term={}, total={}'.format(coeff, term, total))
    return total % M

def get_prime_count_in_factorial(n, p):
    '''
    Find count of p in n!
    floor(n/p) + floor(n/p^2) + floor(n/p^3) + ... ... [until it becomes zero]
    '''
    total = 0
    while n > 0:
        n = n // p
        total += n
    return total


def get_digit_count_in_factorial(n):
    logvalues = [math.log10(i) for i in range(1, n+1)]
    total = sum(logvalues)
    total = math.floor(total) + 1
    return total


def combination1(n, r):
    r = min(r, n-r)
    denominator = [i for i in range(r, 0, -1)]
    numerator = [i for i in range(n, n-r, -1)]

    if sum(denominator) == 0 and sum(numerator) == 0:
        return 1

    print(numerator)
    print(denominator)
    print('-' * 20)

    i = 0
    while i < len(denominator):
        j = 0
        while denominator[i] > 1 and j < len(numerator):
            g = gcd(numerator[j], denominator[i])
            numerator[j] //= g
            denominator[i] //= g
            j += 1
        i += 1

        print(numerator)
        print(denominator)
        print('-' * 20)

    t = 1
    for i in numerator:
        t *= i

    return t


def combination2(n, r, table=None, level=0):
    '''
    A recursive implementation but very ugly.
    '''
    if table == None:
        table = [[0 for i in range(r+1)] for i in range (n+1)]
        table[0][0] = 1

    if n < 0 or r < 0:
        return 0

    if n < r:
        return table[n][r]

    print(' '*level + "Before: n={0} r={1} table[{0}][{1}]={2}".format(n,r,table[n][r]))

    if table[n][r] == 0:
        table[n][r] = combination2(n-1, r, table, level+2) + combination2(n-1, r-1, table, level+2)
        print(' '*level + "After: n={0} r={1} table[{0}][{1}]={2}".format(n,r,table[n][r]))

    return table[n][r]


def print_ncr(ncr, n, r):
    for row in ncr:
        for i in row:
            print('{}'.format(i), end=' ')
        print('')


def combination3(n, r):
    ncr = [[0 for i in range(r+1)] for i in range (n+1)]
    ncr[0][0] = 1

    #i = 1
    #while i <= n:
    for i in range(1, n+1):
        #j = 0
        #while j <= r:
        for j in range(r+1):
            if j > i:
                ncr[i][j] = 0
            elif j == i or j == 0:
                ncr[i][j] = 1
            else:
                ncr[i][j] = ncr[i-1][j] + ncr[i-1][j-1]
            #j += 1
        print_ncr(ncr, n, r)
        print('-' * 80)
        #i += 1

    return ncr



def get_derangement_number_recursion(n):
    if n == 0 or n == 1:
        return 0
    if n == 2:
        return 1

    return (n-1) * (get_derangement_number_recursion(n-2) + get_derangement_number_recursion(n-1))


def get_derangement_number_iteration(n):
    Dn = [0 for i in range(n+1)]
    Dn[2] = 1

    for i in range(3, n+1):
        Dn[i] = (i-1)*(Dn[i-2] + Dn[i-1])
    return Dn


def get_catalan_number(n):
    '''
    I have no idea how the theory works. Just implementing the code.
    '''
    ncr = combination3(2*n, n+1)
    print(ncr[2*n][n])
    print(ncr[2*n][n+1])

    Cn = ncr[2*n][n] - ncr[2*n][n+1]
    return Cn


def get_stirling_number_of_second_kind(n, k):
    '''
    Divide n different things into k divisions.
    '''
    Stnk = [[0 for i in range(k+1)] for i in range (n+1)]
    print(Stnk)
    for i in range(1, n+1):
        for j in range(1, k+1):
            if j == 1 or i == j:
                Stnk[i][j] = 1
            else:
                Stnk[i][j] = Stnk[i-1][j-1] + j * Stnk[i-1][j]
        print(Stnk)
    print(Stnk)




'''
I did not understand the modular inverse thing. Need more reading material.

Then to find the value of C(n,r) mod p = (n! mod p) * ModuloInverse(r! mod p, p) * ModulInverse((n-r)! mod p, p) when p is prime.

What's Lucas' Theorem for combination?

'''

'''
2
xy

4
xxyy
xyxy

6
xxxyyy
xxyxyy

xyxxyy
xyxyxy

xxyyxy

-------

x    y
xx   y
xy   y
'''
