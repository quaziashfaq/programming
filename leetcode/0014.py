#!/usr/bin/env python3

from typing import *

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # common prefix
        cp = []
        minlen = min([len(s) for s in strs])
        if minlen == 0:
            return ''

        for i in range(minlen):
            match = True
            ch = strs[0][i]
            for j in range(1, len(strs)):
                if ch != strs[j][i]:
                    match = False
                    break
            if match:
                cp.append(ch)
            else:
                break

        return ''.join(cp)



if __name__ == '__main__':
    s = Solution()
    print(s.longestCommonPrefix(["flower","flow","flight"]))
