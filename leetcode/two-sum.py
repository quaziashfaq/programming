#!/usr/bin/env python3

# Site: Leetcode
# Problem no:
# Title: Two Sum

from typing import *

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        differences = {}
        '''
        Then find the difference from target value.
        Then check if the difference is in dict.
        Enter n.
        '''
        for i, n in enumerate(nums):
            diff = target - n
            if diff in differences:
                return [differences[diff], i]
            differences[n] = i


    def twoSum_On2(self, nums: List[int], target: int) -> List[int]:
        i = 0
        j = 0
        while i < len(nums):
            j = i + 1
            while j < len(nums):
                if nums[i] + nums[j] == target:
                    return [i, j]
                j = j + 1
            i = i + 1


def main():
    s = Solution()
    assert s.twoSum([6, 5, 4, 3, 2, 1], 10) == [0, 2], "Wrong result"


if __name__ == '__main__':
    main()
