#!/usr/bin/env python3

# Site: Leetcode
# Problem no:
# Title: Valid Palindrome

from typing import *

class Solution:
    def isPalindrome(self, s: str) -> bool:
        '''
        This function checks if a string is a palindrome
        Time complexity: O(n)
        '''

        '''
        Lower case the characcters.
        Take only the alhanumeric characters
        '''
        s = ''.join( [x.lower() for x in s if x.isalnum()] ) # O(n)

        low = 0
        high = len(s) - 1
        '''
        If I am able to find that s[low] and s[high] mismatches
        before I cross the midpoint (that means low is lower than high)
        then the string is not a palindrome.
        '''

        # O(n)
        while low < high:
            if s[low] != s[high]:
                return False
            low += 1
            high -= 1

        '''
        I didn't find any mismatches and
        I have crossed midpoint so it's a valid palindrome.
        '''
        return True


def main():
    s = Solution()
    assert s.isPalindrome('madam') == True
    assert s.isPalindrome('maddam') == True
    assert s.isPalindrome('maddtam') == False


if __name__ == '__main__':
    main()
