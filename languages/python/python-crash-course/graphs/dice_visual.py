#!/usr/bin/env python3

from die import Die
import plotly.express as px

die_1 = Die()
die_2 = Die()

results = []

# roll the dice and generate the results
for roll_num in range(1000):
    result = die_1.roll() + die_2.roll()
    results.append(result)

# Analyze the results.
max_result = die_1.num_sides + die_2.num_sides
frequencies = []
poss_results = range(2, max_result+1)
for value in poss_results:
    frequency = results.count(value)
    frequencies.append(frequency)

# Visualize the results
title = 'Results of Rolling Two D6 Dice 1,000 times'
labels = {'x': 'Result', 'y': 'Frequency of Result'}
fig = px.bar(x=poss_results, y=frequencies, title=title, labels=labels)
fig.update_layout(xaxis_dtick=1)
fig.show()

print(frequencies)
