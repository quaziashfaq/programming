#!/usr/bin/env python3

from typing import *


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        nums3 = [0 for i in range(m+n)]
        i = 0
        j = 0
        k = 0
        while i < m and j < n:
            if nums1[i] <= nums2[j]:
                nums3[k] = nums1[i]
                i += 1
                k += 1
            elif nums1[i] > nums2[j]:
                nums3[k] = nums2[j]
                j += 1
                k += 1

        while i < m:
            nums3[k] = nums1[i]
            i += 1
            k += 1

        while j < n:
            nums3[k] = nums2[j]
            j += 1
            k += 1

        for k in range(m+n):
            nums1[k] = nums3[k]

        return nums1

if __name__ == '__main__':
    s = Solution()
    print(s.merge(nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3))
    print(s.merge(nums1 = [1], m = 1, nums2 = [], n = 0))
    print(s.merge(nums1 = [0], m = 0, nums2 = [1], n = 1))
