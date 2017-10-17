from geopy.geocoders import Nominatim
import pandas

df=pandas.read_csv("supermarkets.csv")
nim=Nominatim()
df["Address"]=df["Address"]+", "+df["City"]+", "+df["State"]+", "+df["Country"]

df["Coordinates"]=df["Address"].apply(nim.geocode)

df["latitude"]=df["Coordinates"].apply(lambda x:x.latitude if x!=None else None)
df["longitude"]=df["Coordinates"].apply(lambda x:x.longitude if x!=None else None)
print(df)
"""
print(nim.geocode("Airport,Kanpur,Uttar Pradesh"))"""
