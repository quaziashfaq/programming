#!/usr/bin/env python3

from pathlib import Path
from datetime import datetime
import csv

import matplotlib.pyplot as plt

path = Path('./sitka_weather_2021_simple.csv')
lines = path.read_text().splitlines()

reader = csv.reader(lines)
header_row = next(reader)
print(header_row)

for index, col_header in enumerate(header_row):
    print(index, col_header)


dates = []
highs = []
lows = []

for row in reader:
    date = datetime.strptime(row[2], '%Y-%m-%d')
    high = int(row[4])
    low = int(row[5])

    dates.append(date)
    highs.append(high)
    lows.append(low)

#print(highs)

plt.style.use('seaborn-v0_8')
fig, ax = plt.subplots()
ax.set_yscale('linear')
ax.set_ylim(10, 140)
ax.plot(dates, highs, color='red', alpha=0.5)
ax.plot(dates, lows, color='blue', alpha=0.5)
ax.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)



ax.set_title('Daily high temperature, 2021', fontsize=24)
ax.set_xlabel('', fontsize=16)
fig.autofmt_xdate()
ax.set_ylabel('Temperature (F)', fontsize=16)
ax.tick_params(labelsize=16)
plt.show()