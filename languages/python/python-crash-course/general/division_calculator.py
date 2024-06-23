#!/usr/bin/env python3

print('Give me to 2 numbers to divide.\nEnter "q" to quit.')

while True:
    first_number = input('\nFirst number: ')
    if first_number == 'q':
        break

    second_number = input('Second number: ')
    if second_number == 'q':
        break

    try:
        answer = int(first_number) / int(second_number)
    except ZeroDivisionError:
        print('You cannot divide by 0!')
    else:
        print(answer)
