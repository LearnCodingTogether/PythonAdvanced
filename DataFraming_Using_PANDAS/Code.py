import os
import pandas

#to list all the files in the directory
print(os.listdir())

#to load csv files
df1=pandas.read_csv("supermarkets.csv")
print(df1)


#to load json files
df2=pandas.read_json("supermarkets.json")
df2=df2.set_index("ID")
print(df2)


#to read excel files
df3=pandas.read_excel("supermarkets.xlsx",sheetname=0)
print(df3)


#to read comma separated files
df4=pandas.read_csv("supermarkets-commas.txt")
print(df4)


#to read semi-colon separated files
df5=pandas.read_csv("supermarkets-semi-colons.txt",sep=";")
print(df5)
