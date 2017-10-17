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

fgv=folium.FeatureGroup(name="Volcanoes")

#using latitude,longitude,elevation and name to create marker as well as popup
#print(list(zip(lat,lon,elev,name)))
for lt,ln,nm1,el in zip(lat,lon,name1,elev):
     #to change marker as a circle
     fgv.add_child(folium.CircleMarker(location=[lt,ln],popup=folium.Popup(str(nm1)+"-"+str(el)+"m", parse_html=True) ,
      radius=6,fill=True,color="grey",fill_color=color_produce(el),fill_opacity=float(0.7)))


fgp=folium.FeatureGroup(name="Populations")
fgp.add_child(folium.GeoJson(data=open("world.json","r",encoding="utf-8-sig").read(),
               style_function=lambda x: {'fillColor':"green" if x['properties']['POP2005']<10000000
               else 'orange' if 10000000<=x['properties']['POP2005']<20000000 else 'red'}))



map.add_child(fgv)
map.add_child(fgp)
#to control layers
map.add_child(folium.LayerControl())

map.save("Map3.html")
