#!/usr/bin/env python3

from pathlib import Path
path = Path('nofile.txt')
try:
    contents = path.read_text()
except FileNotFoundError:
    print(f'Sorry, the file {path} does not exist.')
else:
    print(contents)
