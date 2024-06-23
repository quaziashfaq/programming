#!/usr/bin/env python3

# Quazi Ashfaq
# 10/12/2022
# Python Crash Course

# Strings

first_name = 'shamima'
last_name = 'akther'
full_name = f'{first_name} {last_name}'
print(full_name)
print(f'Hello {full_name.title()}!!')

language = '   python   '
print(f'test {language} test')
print(f'test {language.rstrip()} test')
print(f'test {language.lstrip()} test')
print(f'test {language.strip()} test')

url = 'https://www.google.com'
print(url.removeprefix('https://'))

famous_person = 'albert einstein'
message = f'{famous_person.title()} once said, "A person who never made a mistake never tried anything new."'
print(message)

filename = 'python.txt'
print(filename.removesuffix('.txt'))

# Multiple variable assignment
x, x, x = 0, 1, 2
print(x)

def make_titlecase(astring):
    return astring.title()


bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles)
print(f'I have different kinds of bicycles, such as: { ", ".join(map(make_titlecase, bicycles[:-1]))} and {map(make_titlecase, bicycles[-1])}')

# Suggested code may be subject to a license. Learn more: ~LicenseLog:3830668213.
cars = ['bmw', 'audi', 'toyota', 'subaru']
print(cars)
print(sorted(cars, reverse=True))
print(cars)

for car in cars:
    if car == 'bmw':
        print(f'I would like to own a {car.upper()}')
    else:
        print(f'I also like the {car.title()}')

t = range(10)
print(t)

import random

#friends = {
#        'progga': {
#            'first_name': 'Khalid',
#            'last_name': 'Adnan',
#            'city': 'London',
#            },
#        'shahid': { 
#            'first_name': 'Shahiduz',
#            'last_name': 'Zaman',
#            'city': 'Melbourne',
#            },
#        }

# changed from declarative variable to build model
def make_friend(first_name, last_name, city):
    return {
            'first_name': first_name,
            'last_name': last_name,
            'city': city,
            }

friends = {}
friends['progga'] = make_friend('khalid', 'adnan', 'london')
friends['shahid'] = make_friend('shahiduz', 'zaman', 'melbourne')

print('Here are names and cities of some friends.')
for friend, friend_info in friends.items():
    #details = friends[friend]
    #print(details)
    print(f"{friend.title()} is my friend. His full name is {friend_info['first_name'].title()} {friend_info['last_name'].title()}. He lives in {friend_info['city'].title()}.")



def city_country(city, country):
    return f'{city.title()}, {country.title()}'

active = True
while active:
    city = input('Enter a city: ')
    country = input('Enter the country the city is in: ')

    print(city_country(city, country))

    message = input('Do you want to continue? (y/n): ')
    if message == 'n':
        active = False
