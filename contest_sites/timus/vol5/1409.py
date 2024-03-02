#!/usr/bin/env python3

harry_shot, larry_shot = [int(i) for i in input().strip().split()]

total = harry_shot + larry_shot
total = total - 1
print(total-harry_shot, total-larry_shot)
