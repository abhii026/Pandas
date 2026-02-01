import pandas as ab

data={
    "Name":['Abhi','Jeet','Jai'],
    "Age":[20,22,21],
    "City":['Varansi','Jodhpur','Faridabad']
}
df=ab.DataFrame(data)
print(df)

#df.to_csv("output.csv")  it save files with index.
# df.to_csv("output.csv",index=False)

#to save in excel
# df.to_excel("output.xlsx",index=False)

#to save as json
df.to_json("output.json",index=False)