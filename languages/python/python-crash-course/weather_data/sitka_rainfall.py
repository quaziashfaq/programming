#!/usr/bin/env python3

from pathlib import Path
from datetime import datetime
import csv

import matplotlib.pyplot as plt

path = Path('./sitka_weather_2021_full.csv')
lines = path.read_text().splitlines()

reader = csv.reader(lines)
header_row = next(reader)
print(header_row)

for index, col_header in enumerate(header_row):
    print(index, col_header)


dates = []
rainfalls = []

for row in reader:
    current_date = datetime.strptime(row[2], '%Y-%m-%d')
    try:
        rainfall = float(row[5])
    except:
        print(f'Data missing for {current_date}')
    else:
        dates.append(current_date)
        rainfalls.append(rainfall)

#print(highs)

plt.style.use('seaborn-v0_8')
fig, ax = plt.subplots()
#ax.plot(dates, highs, color='red', alpha=0.5)
ax.plot(dates, rainfalls, color='blue', alpha=0.5)
#ax.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)


ax.set_title('Daily rainfall, 2021', fontsize=24)
ax.set_xlabel('', fontsize=16)
fig.autofmt_xdate()
ax.set_ylabel('Rainfall', fontsize=16)
ax.tick_params(labelsize=16)
plt.show()
