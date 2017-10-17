import pandas

df1=pandas.read_json("supermarkets.json")
df1=df1.set_index("Address")

#use of loc
print(df1.loc["735 Dolores St":"3995 23rd St","Country":"ID"])
print(df1.loc["735 Dolores St":"3995 23rd St","Country"])
print(list(df1.loc[:,"Country"]))


#use of iloc
print(df1.iloc[1:3,2:4])
print(df1.iloc[1:3,4])
print(list(df1.iloc[:,2]))


#use of ix
print(df1.ix[3,"Name"])
print(df1.ix[3,4])
