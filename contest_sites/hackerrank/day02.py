#!/usr/bin/python3

import math
import os
import random
import re
import sys

# Complete the solve function below.
def solve(meal_cost, tip_percent, tax_percent):
    tip = meal_cost * tip_percent / 100
    tax = meal_cost * tax_percent / 100
    total_cost = meal_cost + tip + tax

    cent = total_cost - int(total_cost)
    if cent <0.5:
        total_cost = int(math.floor(total_cost))
    else:
        total_cost = int(math.ceil(total_cost))

    if total_cost <= 1:
        print('The total meal cost is ' + str(total_cost) + ' dollar.')
    else:
        print('The total meal cost is ' + str(total_cost) + ' dollars.')

if __name__ == '__main__':
    meal_cost = float(input())
    tip_percent = int(input())
    tax_percent = int(input())
    solve(meal_cost, tip_percent, tax_percent)
