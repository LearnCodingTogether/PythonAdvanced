import folium
import pandas

data=pandas.read_csv("Volcanoes_USA.txt")
lat=list(data["LAT"])
lon=list(data["LON"])
elev=list(data["ELEV"])
name1=list(data["NAME"])

#customising marker color on the basis of elevation
def color_produce(elevation):
    if elevation<1000:
        return 'green'
    elif elevation>=1000 and elevation<3000:
        return 'orange'
    else:
        return 'red'


#to create and save map using longitude and latitude
map=folium.Map(location=[38.58,-99.09], zoom_start=6, tiles="Mapbox Bright")

fg=folium.FeatureGroup(name="My Map")

#using latitude,longitude,elevation and name to create marker as well as popup
#print(list(zip(lat,lon,elev,name)))
for lt,ln,nm1,el in zip(lat,lon,name1,elev):

    fg.add_child(folium.Marker(location=[lt,ln],popup=folium.Popup(str(nm1)+"-"+str(el)+"m", parse_html=True) ,
     icon=folium.Icon(color=color_produce(el))))
     #to change marker as a circle
    fg.add_child(folium.CircleMarker(location=[lt,ln],popup=folium.Popup(str(nm1)+"-"+str(el)+"m", parse_html=True) ,
      radius=6,fill=True,color="grey",fill_color=color_produce(el),fill_opacity=float(0.7)))
map.add_child(fg)
map.save("Map2.html")
