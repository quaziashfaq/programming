#!/usr/bin/env python3

guests = ['progga', 'shahid', 'panna', 'jahangir']

print(f'\nList of invited guests ({len(guests)}): ', end='')
print(guests)

print('panna cannot make it')
guests.remove('panna')

print(f'\nList of invited guests ({len(guests)}): ', end='')
print(guests)


print('\nI have found a bigger table')
guests.insert(0, 'suhrid')
guests.insert(3, 'farhan')
guests.append('mostofa')

print(f'\nList of invited guests ({len(guests)}): ', end='')
print(guests)


print('\nMy table will not arrive timely')
print('\nRemoving some guests...')
print(guests.pop())
print(guests.pop())
print(guests.pop())
print(guests.pop())


print(f'\nList of invited guests ({len(guests)}): ', end='')
print(guests)


print('\nRemoving the remaining guests now...')
del(guests[1])
del(guests[0])
print(f'\nList of invited guests ({len(guests)}): ', end='')
print(guests)
