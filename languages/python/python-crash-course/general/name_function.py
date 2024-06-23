#!/usr/bin/env python3

def get_formatted_name(first, last, middle=''):
    '''Generate a neatly formatted full time.'''
    if middle:
        full_name = f'{first} {middle} {last}'.title()
    else:
        full_name = f'{first} {last}'.title()

    return full_name
