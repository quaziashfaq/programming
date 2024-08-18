#!/usr/bin/env python3

from pathlib import Path
from datetime import datetime
import csv
import matplotlib.pyplot as plt


'''
I combined the exercise 16-2.
I compared the weather data of 2 locations.
The indexes are programmatically found. Not hardcoded. (partial of 16-4)
Date: Sun 18 Aug 2024
'''

def open_file(path):
    '''It opens the csv file and returns the reader object'''
    csv_data = Path(path)
    lines = csv_data.read_text().splitlines()
    reader = csv.reader(lines)
    return reader

def get_column_locations(reader, column_headers):
    '''It finds the column_header locations and returns a dictionary of column_headers and restof the reader data as a dictionary.'''
    header_row = next(reader)
    print(type(header_row))
    column_header_locations = {}
    for header in column_headers:
        column_header_locations[header] = header_row.index(header)

    return column_header_locations



def get_weather_data_from_reader(reader, colhl):
    '''
    get the dates, highs and lows from the reader.
    the column header locations are defined in colhl dict.
    It returns the weather data as dict.
    '''

    dates, highs, lows = [], [], []

    for row in reader:
        current_date = datetime.strptime(row[colhl['DATE']], '%Y-%m-%d')
        try:
            high = int(row[colhl['TMAX']])
            low = int(row[colhl['TMIN']])
        except:
            print(f'Value error in {current_date}')
        else:
            dates.append(current_date)
            highs.append(high)
            lows.append(low)

    return {'DATES': dates, 'HIGHS': highs, 'LOWS': lows}


def get_weather_data_from_file(csv_filename):
    reader = open_file(csv_filename)
    col_hdr = ['DATE', 'TMAX', 'TMIN']
    col_hdr_loc = get_column_locations(reader, col_hdr)
    print(col_hdr_loc)
    return get_weather_data_from_reader(reader, col_hdr_loc)


sitka_weather_data = get_weather_data_from_file('./sitka_weather_2021_simple.csv')
#print(sitka_weather_data)
death_valley_weather_data = get_weather_data_from_file('./death_valley_2021_simple.csv')
#print(death_valley_weather_data)

plt.style.use('seaborn-v0_8')
fig, ax = plt.subplots()
ax.set_yscale('linear')
ax.set_ylim(10, 140)

def plot_data(ax, wd, fill_color): 
    '''wd means weather_data. ax means axes.'''
    dates, highs, lows = wd['DATES'], wd['HIGHS'], wd['LOWS']
    #ax.plot(dates, highs, color='red', alpha=0.5)
    #ax.plot(dates, lows, color='blue', alpha=0.5)
    ax.fill_between(dates, highs, lows, facecolor=fill_color, alpha=0.1)

plot_data(ax, sitka_weather_data, 'blue')
plot_data(ax, death_valley_weather_data, 'green')

ax.set_title('Daily high temperature, 2021', fontsize=24)
ax.set_xlabel('', fontsize=16)
fig.autofmt_xdate()
ax.set_ylabel('Temperature (F)', fontsize=16)
ax.tick_params(labelsize=16)
plt.show()
