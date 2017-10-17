#program to update row and column
import pandas

df=pandas.read_json("supermarkets.json")
df=df.set_index("Address")

#Program to add column and modify
df["Continent"]=df.shape[0]*["North America"]
df["Continent"]=df["Country"]+","+"North America"


#to add a row we have to take a transpose of the data then  add the entries as column and then transpose again
df1=df.T
df1["Nagar Nigam"]=["Saharanpur","India",12,7,"Banwali","Uttar Pradesh","Asia"]
df=df1.T
print(df)
