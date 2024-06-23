#!/usr/bin/env python3

from city_functions import get_formatted_city_country

def test_city_country():
    msg = get_formatted_city_country('dhaka', 'bangladesh')
    assert msg == 'Dhaka, Bangladesh'


def test_city_country_population():
    msg = get_formatted_city_country('dhaka', 'bangladesh', 180_000_000)
    assert msg == 'Dhaka, Bangladesh - population {population}'


    msg = get_formatted_city_country('dhaka', 'bangladesh', 0)
