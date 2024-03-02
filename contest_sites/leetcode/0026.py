#!/usr/bin/env python3

from typing import *

'''
Given an integer array nums sorted in non-decreasing order,
remove the duplicates in-place such that each unique element appears only once.
The relative order of the elements should be kept the same.
'''

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 0       # To traverse the array.
        k = 0       # k will point to the unique values.
        l = len(nums)

        while i < l:
            j = i       # j will point to 1st value of duplicates

            # Then go past all the duplicates.
            while i < l and nums[i] == nums[j]:
                i += 1

            # Then put the value from j to k
            nums[k] = nums[j]
            k += 1
        return k
