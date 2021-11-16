#!/usr/bin/env python3
#
from typing import *

class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        elif x >=0 and x < 10:
            return True
        else:
            num = str(x)
            left = 0
            right = len(num) - 1
            while left <= right:
                if num[left] != num[right]:
                    return False
                left += 1
                right -= 1
            return True
