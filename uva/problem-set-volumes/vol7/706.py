#!/usr/bin/env python3

import sys

def lcd_display(arr):
    for each_row in arr:
        print(''.join(each_row))

def make_a_grid(n, ch): 
    rows = 2 * n + 3 
    cols = n + 2
    arr = []
    for i in range(rows):
        arr.append([ch for j in range(cols)])
    return arr

def fill_in_horizontal_line(arr, row, ch):
    for i in range(1, len(arr[row])-1):
        arr[row][i] = ch

def fill_in_top_line(arr, ch):
    top_line = 0
    fill_in_horizontal_line(arr, top_line, ch)

def fill_in_middle_line(arr, ch):
    middle_line = len(arr) // 2
    fill_in_horizontal_line(arr, middle_line, ch)

def fill_in_last_line(arr, ch):
    last_line = len(arr) - 1
    fill_in_horizontal_line(arr, last_line, ch)

def fill_in_vertical_line(arr, col, pos, ch):
    if pos == 0: # top
        starting_row = 1
        end_row = len(arr) // 2
    elif pos == 1: # bottom
        starting_row = len(arr) // 2 + 1
        end_row = len(arr) - 1
    
    for i in range(starting_row, end_row):
        arr[i][col] = ch
    return arr


def fill_in_vertical_line_top(arr, col, ch):
    return fill_in_vertical_line(arr, col, 0, ch)

def fill_in_vertical_line_bottom(arr, col, ch):
    return fill_in_vertical_line(arr, col, 1, ch)
    
def fill_in_vertical_line_top_left(arr, ch):
    return fill_in_vertical_line_top(arr, 0, ch)

def fill_in_vertical_line_top_right(arr, ch):
    return fill_in_vertical_line_top(arr, len(arr[0])-1, ch)

def fill_in_vertical_line_bottom_left(arr, ch):
    return fill_in_vertical_line_bottom(arr, 0, ch)

def fill_in_vertical_line_bottom_right(arr, ch):
    return fill_in_vertical_line_bottom(arr, len(arr[0])-1, ch)



def get_numbers_in_lcd():
    numbers = [
        get_0,
        get_1,
        get_2,
        get_3,
        get_4,
        get_5,
        get_6,
        get_7,
        get_8,
        get_9
    ]
    def get_number(num, gird_size):
        arr = make_a_grid(gird_size, ' ')
        return numbers[num](arr)
    return get_number



def get_0(arr):
    chdot = ' '
    chdash = '-'
    chv = '|'
    fill_in_top_line(arr, chdash)
    fill_in_last_line(arr, chdash)
    fill_in_vertical_line_top_left(arr, chv)
    fill_in_vertical_line_top_right(arr, chv)
    fill_in_vertical_line_bottom_left(arr, chv)
    fill_in_vertical_line_bottom_right(arr, chv)
    return arr

def get_1(arr):
    chdot = ' '
    chdash = '-'
    chv = '|'
    fill_in_vertical_line_top_right(arr, chv)
    fill_in_vertical_line_bottom_right(arr, chv)
    return arr

def get_2(arr):
    chdot = ' '
    chdash = '-'
    chv = '|'
    fill_in_top_line(arr, chdash)
    fill_in_middle_line(arr, chdash)
    fill_in_last_line(arr, chdash)
    fill_in_vertical_line_top_right(arr, chv)
    fill_in_vertical_line_bottom_left(arr, chv)
    return arr

def get_3(arr):
    chdot = ' '
    chdash = '-'
    chv = '|'
    fill_in_top_line(arr, chdash)
    fill_in_middle_line(arr, chdash)
    fill_in_last_line(arr, chdash)
    fill_in_vertical_line_top_right(arr, chv)
    fill_in_vertical_line_bottom_right(arr, chv)
    return arr

def get_4(arr):
    chdot = ' '
    chdash = '-'
    chv = '|'
    
    fill_in_middle_line(arr, chdash)
    fill_in_vertical_line_top_left(arr, chv)
    fill_in_vertical_line_top_right(arr, chv)
    fill_in_vertical_line_bottom_right(arr, chv)
    return arr

def get_5(arr):
    chdot = ' '
    chdash = '-'
    chv = '|'
    fill_in_top_line(arr, chdash)
    fill_in_middle_line(arr, chdash)
    fill_in_last_line(arr, chdash)
    fill_in_vertical_line_top_left(arr, chv)
    fill_in_vertical_line_bottom_right(arr, chv)
    return arr

def get_6(arr):
    chdot = ' '
    chdash = '-'
    chv = '|'
    fill_in_top_line(arr, chdash)
    fill_in_middle_line(arr, chdash)
    fill_in_last_line(arr, chdash)
    fill_in_vertical_line_top_left(arr, chv)
    fill_in_vertical_line_bottom_left(arr, chv)
    fill_in_vertical_line_bottom_right(arr, chv)
    return arr

def get_7(arr):
    chdot = ' '
    chdash = '-'
    chv = '|'
    fill_in_top_line(arr, chdash)
    fill_in_vertical_line_top_right(arr, chv)
    fill_in_vertical_line_bottom_right(arr, chv)
    return arr

def get_8(arr):
    chdot = ' '
    chdash = '-'
    chv = '|'
    fill_in_top_line(arr, chdash)
    fill_in_middle_line(arr, chdash)
    fill_in_last_line(arr, chdash)
    fill_in_vertical_line_top_left(arr, chv)
    fill_in_vertical_line_top_right(arr, chv)
    fill_in_vertical_line_bottom_left(arr, chv)
    fill_in_vertical_line_bottom_right(arr, chv)
    return arr

def get_9(arr):
    chdot = ' '
    chdash = '-'
    chv = '|'
    fill_in_top_line(arr, chdash)
    fill_in_middle_line(arr, chdash)
    fill_in_last_line(arr, chdash)
    fill_in_vertical_line_top_left(arr, chv)
    fill_in_vertical_line_top_right(arr, chv)
    fill_in_vertical_line_bottom_right(arr, chv)
    return arr



def get_input():
    for line in sys.stdin:
        a, b = list(map(int, line.split()))
        if a == 0 and b == 0:
            return
        yield a, b

def number_to_array(num):
    arr = []
    if num == 0:
        arr.append(0)
    else:
        d = num
        while (d != 0):
            arr.append(d % 10)
            d = d // 10

    return reversed(arr)


def main():
    get_number = get_numbers_in_lcd()

    for l in get_input():
        l = list(l)
        grid_size, number = l
        digit_array = number_to_array(number)
        numbers = []
        for i in digit_array:
            numbers.append(get_number(i, grid_size))

        ns = [] # The whole display string
        nrows = 2 * grid_size + 3
        for i in range(nrows):
            t = []
            for each_digit in numbers:
                t.append(''.join(each_digit[i]))

            #print(t)
            ns.append(' '.join(t))

        for i in ns:
            print(i)
        print('')
        



main() 

