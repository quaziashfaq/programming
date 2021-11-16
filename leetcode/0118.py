#!/usr/bin/env python3

from typing import *

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        triangle = []
        for num in range(1, numRows+1):
            if num == 1:
                line = [1]
            else:
                line = [0 for i in range(num)]
                line[0], line[-1] = 1, 1
                for i in range(1, num-1):
                    line[i] = oldline[i-1] + oldline[i]

            triangle.append(line)
            oldline = line
        return triangle


if __name__ == '__main__':
    s = Solution()
    for i in range(10):
        print(s.generate(i))
