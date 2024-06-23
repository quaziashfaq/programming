#!/usr/bin/env python3

print('Actual list: ', end='')
locations = ['delhi', 'islamabad', 'tokyo', 'sydney', 'auckland']
print(locations)

print('Sorted list: ', end='')
print(sorted(locations))

print('Reversely Sorted list: ', end='')
print(sorted(locations, reverse=True))


print('Actual list: ', end='')
print(locations)

locations.reverse()
print('locations reversed: ', end='')
print(locations)

locations.reverse()
print('locations reversed: ', end='')
print(locations)

locations.sort()
print('Sorted list: ', end='')
print(locations)

locations.sort(reverse=True)
print('Sorted list: ', end='')
print(locations)
