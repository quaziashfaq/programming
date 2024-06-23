#!/usr/bin/env python3

from pathlib import Path

def count_words(path):
    '''Count the number of works in a file'''
    try:
        contents = path.read_text(encoding='utf-8')
    except FileNotFoundError:
        print(f'Sorry. the file {path} does not exist.')
    else:
        words = contents.split()
        num_words = len(words)
        print(f'The file {path} has {num_words} of words.')


filenames = ['alice.txt', 'siddahartha.txt', 'moby_dick.txt']
for filename in filenames:
    path = Path(filename)
    count_words(path)
