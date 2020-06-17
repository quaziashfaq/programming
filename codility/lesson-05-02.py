#!/usr/bin/env python3

def solution(S, P, Q):
    genomic_bits = {
        'A': 1,
        'C': 2,
        'G': 3,
        'T': 4
    }

    n = len(S)
    frequency = [[0 for i in range(5)] for i in range(n)]

    for i in range(n):
        frequency[i][genomic_bits[S[i]]] = 1

    # counting prefix sums of the frequency table
    # i.e. calculating frequency of characters in nth position

    for i in range(1,n):
        for j in range(1,5):
            frequency[i][j] += frequency[i-1][j]


    print(frequency)
    results = []
    for x,y in zip(P, Q):
        print(x,y)
        if x == y:
            results.append(genomic_bits[S[x]])
        elif x == 0:
            for i in range(1,5):
                if frequency[y][i] > 0:
                    results.append(i)
                    break
        else:
            x = x - 1
            for i in range(1, 5):
                d = frequency[y][i] - frequency[x][i]
                if d > 0:
                    results.append(i)
                    break
    return(results)



print(solution('CAGCCTA', [0], [0]))
print(solution('CAGCCTA', [0], [1]))
print(solution('CAGCCTA', [0], [2]))
print(solution('CAGCCTA', [0], [3]))
print(solution('CAGCCTA', [2], [5]))
print(solution('CAGCCTA', [2, 5, 0], [4, 5, 6]))
print(solution('AC', [0, 0, 1], [0, 1, 1]))
