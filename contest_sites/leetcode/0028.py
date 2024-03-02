#!/usr/bin/env python3

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle == '':
            return 0

        found_index = -1
        i_haystack = 0
        len_needle = len(needle)
        li_haystack = len(haystack) -  len_needle + 1

        while i_haystack < li_haystack:
            if haystack[i_haystack:i_haystack+len_needle] == needle:
                found_index = i_haystack
                break
            i_haystack += 1

        return found_index


if __name__ == '__main__':
    s = Solution()
    print(s.strStr('hello', 'll'))
    print(s.strStr('helolo', 'll'))
    print(s.strStr('helolo', ''))
    print(s.strStr('', 'll'))
    print(s.strStr('', ''))

    f = open('0028_input.txt')
    haystack = f.readline().strip()
    needle = f.readline().strip()

#    print(haystack)
#    print(len(haystack))
    print(s.strStr(haystack, needle))
