#!/usr/bin/env python3

from name_function import get_formatted_name

def test_first_last_name():
    '''Does name "Quazi Ashfaq" work?'''
    formatted_name = get_formatted_name('quazi', 'ashfaq')
    assert formatted_name == 'Quazi Ashfaq'


def test_first_middle_last_name():
    '''Does name "Quazi Ashfaq" work?'''
    formatted_name = get_formatted_name('quazi', 'rahman', 'ashfaq')
    assert formatted_name == 'Quazi Ashfaq Rahman'
