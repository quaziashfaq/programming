#!/usr/bin/env python3

from pathlib import Path

path = Path('./pi_million_digits.txt')
contents = path.read_text().rstrip()

pi_string = ''
lines = contents.splitlines()
for line in lines:
    pi_string += line.strip()

#print(pi_string)
print(len(pi_string))

print('200882' in pi_string)
print('200880' in pi_string)

print('082082' in pi_string)
print('082080' in pi_string)

