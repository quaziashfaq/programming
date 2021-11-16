#!/usr/bin/env python3
#
from typing import *

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        differences = {}
        '''
        Take a number from the nums list.
        Then find the difference from target value.
        Then check if the difference is in dict.
        If yes, we found the 2 values from the array whose sum equals to target.
        Otherwise, keep the index of the value in the value-indexed dictionary.
        '''
        for i, n in enumerate(nums):
            diff = target - n
            if diff in differences:
                return [differences[diff], i]
            differences[n] = i


def main():
    s = Solution()
    assert s.twoSum([3, 2, 4], 6) == [1, 2]
    assert s.twoSum([2, 7, 11, 15], 9) == [0, 1]
    assert s.twoSum([7, 11, 15, 2], 9) == [0, 3]

if __name__ == '__main__':
    main()
