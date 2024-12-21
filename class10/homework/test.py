# Name: Owen Shi
# Date: Sat, Nov. 16th
# Assignment 41

import folium
import pandas as pd

input_file = input("Enter CSV file name: ")
output_file = input("Enter output file: ")

map = folium.Map(location=[40.75, -74.125],
                 zoom_start=10, tiles="Cartodb Positron")

df = pd.read_csv(input_file)

for _, row in df.iterrows():
    folium.Marker([row["LATITUDE"], row["LONGITUDE"]],
                  popup=row["TIME"]).add_to(map)

map.save(outfile=output_file)
