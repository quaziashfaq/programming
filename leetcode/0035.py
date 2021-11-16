#!/usr/bin/env python3

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        start = 0
        end = len(nums) - 1

        while start <= end:
            mid = (start + end ) // 2
            if target == nums[mid]:
                return mid
            elif target < nums[mid]:
                end = mid - 1
            elif target > nums[mid]:
                start = mid + 1
        return start

def main():
    s = Solution()
    assert s.searchInsert(nums = [1, 3, 5, 6], target = 7) == 4

if __name__ == "__main__":
    main()
