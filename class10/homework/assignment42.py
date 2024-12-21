# Name: Owen Shi
# Date: Sat, Nov. 16th
# Assignment 42

import folium
import pandas as pd

input_file = input("Enter CSV file name: ")
output_file = input("Enter output file: ")

map = folium.Map(location=[40.75, -74.125],
                 tiles="Cartodb Positron", zoom_start=10)

df = pd.read_csv(input_file)

for index, row in df.iterrows():
    lat = row["LATITUDE"]
    long = row["LONGITUDE"]

    folium.Marker(
        [row["LATITUDE"], row["LONGITUDE"]],
        popup=row["CRASH TIME"],
    ).add_to(map)

map.save(outfile=output_file)
