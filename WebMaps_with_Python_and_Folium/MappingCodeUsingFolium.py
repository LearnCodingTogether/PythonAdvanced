import folium

#to create and save map using longitude and latitude
map=folium.Map(location=[28.54,77.35], zoom_start=6)

fg=folium.FeatureGroup(name="My Map")

for coordinates in ([28.54,77.3],[28.54,77.23],[28.54,77.33]):
    fg.add_child(folium.Marker(location=coordinates,popup="Hi I am a Marker", icon=folium.Icon(color="green")))

map.add_child(fg)
map.save("Map1.html")
