#!/usr/bin/env python3

from pathlib import Path
import json
import os


dir_path = os.path.dirname(os.path.realpath(__file__))
path = Path(dir_path + '/eq_data_1_day_m1.geojson', encoding='utf8')
contents = path.read_text()
all_eq_data = json.loads(contents)

#path = Path('./readable_eq_data.geojson')
#readable_contents = json.dumps(all_eq_data, indent=4)
#path.write_text(readable_contents)

all_eq_dicts = all_eq_data['features']
print(len(all_eq_dicts))


mags = []
for eq_dict in all_eq_dicts:
    mag = eq_dict['properties']['mag']
    mags.append(mag)

print(mags)
print(max(mags))
