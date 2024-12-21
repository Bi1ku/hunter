# Name: Owen Shi
# Date: Sat, Nov. 16th
# Assignment 41

import folium

map = folium.Map(location=[40.75, -74.125], zoom_start=10)

folium.Marker(location=[40.768731, -73.964915],
              popup="Hunter College").add_to(map)

map.save(outfile="nycMap.html")
