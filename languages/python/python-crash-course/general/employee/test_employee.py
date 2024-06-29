#!/usr/bin/env python3

import pytest
from employee import Employee

@pytest.fixture
def employee():
    employee = Employee('quazi', 'ashfaq', 10000)
    return employee

def test_default_raise(employee):
    employee.give_raise()
    assert 15000 == employee.annual_salary


def test_arbitrary_raise(employee):
    employee.give_raise(3000)
    assert 13000 == employee.annual_salary
