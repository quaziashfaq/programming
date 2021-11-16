#!/usr/bin/env python3

from typing import *

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        start = 0
        end = len(numbers) - 1

        while start < end:
            n1 = numbers[start]

            # Calculate what the other could be to meet th etarget
            n2 = target - n1

            '''
            The array is sorted in non-decreasing order.
            So discard numbers from the end of the array which are bigger than n2
            '''
            while start < end and numbers[end] > n2:
                end -= 1

            # The very next number could be either equal to n2
            # or less than n2
            if numbers[end] == n2:
                return [start+1, end+1]

            # If I can't find it, then numbers[end] < n2 and
            # start the next number in the array.
            start += 1


def main():
    s = Solution()
    assert s.twoSum([2, 7, 11, 15], 9) == [1, 2]


if __name__ == '__main__':
    main()
