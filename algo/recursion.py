#!/usr/bin/env python3

def go_up_from_a_to_b(a, b):
    if a > b:
        return
    print(a)
    go_up_from_a_to_b(a+1, b)


def go_down_from_b_to_a(b, a):
    if a > b:
        return
    print(b)
    go_down_from_b_to_a(b-1, a)


def is_string_palindrome(s):
    if len(s) == 0:
        return True
    print(s)
    return (s[0] == s[-1]) and is_string_palindrome(s[1:-1])
    #return is_start_end_string_equal(s[1:-1]) and (s[0] == s[-1])



def is_number_palindrome(n):
    s = str(n)
    return is_string_palindrome(s)

def make_palindrome(n):
    p = list(range(0,10))
    p.extend(range(11,100,11))

    p = list(map(str, p))
    print(p)

    q = []
    for i in range(ord('1'), ord('9')+1):
        for j in p:
            q.append(chr(i) + j + chr(i))
    p.extend(q)

    return p


make_palindrome(10)
