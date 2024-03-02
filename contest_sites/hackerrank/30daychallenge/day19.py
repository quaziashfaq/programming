#!/usr/bin/python3

import math

class AdvancedArithmetic(object):
    def divisorSum(self, n):
        raise NotImplementedError

class Calculator(AdvancedArithmetic):
    def divisorSum(self, n):
        total = 0
        last_divisor = math.ceil(math.sqrt(n))
        if n//last_divisor == last_divisor:
            total += last_divisor

        # print('last divisor, total: %d, %d' % (last_divisor, total))

        for i in range(1, last_divisor):
            if n % i == 0:
                total += i
                total += n // i
                # print(i, n//i, total)

        return total


n = int(input())
my_calculator = Calculator()
s = my_calculator.divisorSum(n)
print("I implemented: " + type(my_calculator).__bases__[0].__name__)
print(s)
