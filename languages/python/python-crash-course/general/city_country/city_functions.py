#!/usr/bin/env python3

def get_formatted_city_country(city, country, population=0):
    msg = f'{city}, {country}'.title()
    if population:
        msg += f' - population {population}'
    return msg
