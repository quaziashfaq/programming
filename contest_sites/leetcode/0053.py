#!/usr/bin/env python3

from typing import *

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        result = [i for i in nums]
        maxsum = result[0]
        i = 1
        #print(result)
        while i < len(result):
            #print(result)
            s = result[i-1] + result[i]
            if result[i] < s:
                result[i] = s
            if maxsum < result[i]:
                maxsum = result[i]
            i += 1
        return maxsum


if __name__ == '__main__':
    s = Solution()
    print(s.maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))
    print(s.maxSubArray([1]))
    print(s.maxSubArray([5,4,-1,7,8]))
