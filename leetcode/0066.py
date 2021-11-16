#!/usr/bin/env python3

from typing import *

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        i = len(digits) - 1
        c = 1
        while i >= 0:
            s = digits[i] + c
            digits[i] = s % 10
            c = s // 10
            if c == 0:
                break
            i -= 1
        if c > 0:
            digits.insert(0, c)

        return digits


if __name__ == '__main__':
    s = Solution()
    print(s.plusOne([1, 2, 3]))
    print(s.plusOne([4, 3, 2, 1]))
    print(s.plusOne([0]))
    print(s.plusOne([9]))
    print(s.plusOne([9, 9, 9]))
