#!/usr/bin/env python3

from typing import *

class Solution:
    def romanToInt(self, s: str) -> int:
        roman = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        num = [0 for i in range(len(s))]
        i = 0
        while i < len(s):
            num[i] = roman[s[i]]
            i += 1

        i = 0
        while i < len(s)-1:
            if num[i] < num[i+1]:
                num[i] = -num[i]
            i += 1

        return sum(num)


if __name__ == '__main__':
    s = Solution()
    print(s.romanToInt('III'))
    print(s.romanToInt('X'))
    print(s.romanToInt('IV'))
    print(s.romanToInt('IX'))
    print(s.romanToInt('LVIII'))
    print(s.romanToInt('MCMXCIV'))
