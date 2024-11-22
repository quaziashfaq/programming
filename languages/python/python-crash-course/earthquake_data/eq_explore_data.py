#!/usr/bin/env python3

from pathlib import Path
import json
import os
import plotly.express as px


#dir_path = os.path.dirname(os.path.realpath(__file__))
#path = Path(dir_path + '/eq_data_1_day_m1.geojson', encoding='utf8')
path = Path('./eq_data_30_day_m1.geojson', encoding='utf8')
contents = path.read_text()
all_eq_data = json.loads(contents)

#path = Path('./readable_eq_data.geojson')
#readable_contents = json.dumps(all_eq_data, indent=4)
#path.write_text(readable_contents)

all_eq_dicts = all_eq_data['features']
print(len(all_eq_dicts))


mags, lons, lats = [], [], []
for eq_dict in all_eq_dicts:
    mag = eq_dict['properties']['mag']
    lon = eq_dict['geometry']['coordinates'][0]
    lat = eq_dict['geometry']['coordinates'][1]

    mags.append(mag)
    lons.append(lon)
    lats.append(lat)

#print(mags)
#print(lons)
#print(lats)

title = 'Global Earthquakes'
fig = px.scatter_geo(lon=lons, lat=lats, 
                     size=mags, 
                     title=title,
                     color=mags,
                     color_continuous_scale="Viridis",
                     labels={'color' : 'Magnitude'},
                     projection='natural earth',
                     )
fig.show()

print(max(mags))
