import pandas

df1=pandas.read_json("supermarkets.json")
df1=df1.set_index("Address")
print(df1)

#Deleting row(0 is for row) having address "3666 21st St"
print(df1.drop("3666 21st St",0))

#drop column(1 is for column) named as City
print(df1.drop("City",1))

#Drop row from 0 to 2
print(df1.drop(df1.index[0:3],0))


#Drop Columns from 0 to 2
print(df1.drop(df1.columns[0:3],1))
