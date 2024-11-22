#!/usr/bin/env python3

from pathlib import Path
import json
import os
import plotly.express as px


#dir_path = os.path.dirname(os.path.realpath(__file__))
#path = Path(dir_path + '/eq_data_1_day_m1.geojson', encoding='utf8')
path = Path('./2024-09-21_earthquake_data.geojson', encoding='utf8')
contents = path.read_text()
all_eq_data = json.loads(contents)

#path = Path('./readable_eq_data.geojson')
#readable_contents = json.dumps(all_eq_data, indent=4)
#path.write_text(readable_contents)

all_eq_dicts = all_eq_data['features']
print(len(all_eq_dicts))


mags, lons, lats, eq_titles = [], [], [], []
for eq_dict in all_eq_dicts:
    mags.append( eq_dict['properties']['mag'] )
    lons.append( eq_dict['geometry']['coordinates'][0] )
    lats.append(  eq_dict['geometry']['coordinates'][1] )
    eq_titles.append(eq_dict['properties']['title'])

for i in range(len(mags)):
    if mags[i] < 0.0:
        print(mags[i])
        mags[i] = 0.0


title = all_eq_data['metadata']['title']
fig = px.scatter_geo(lon=lons, lat=lats, 
                     size=mags, 
                     title=title,
                     color=mags,
                     color_continuous_scale="Viridis",
                     labels={'color' : 'Magnitude'},
                     projection='natural earth',
                     hover_name=eq_titles,
                     )
fig.show()

print(max(mags))

#https://api.github.com/search/repositories/q=language:python+sort:stars
