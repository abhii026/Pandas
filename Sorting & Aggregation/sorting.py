import pandas as pd
data={
    "Name":['Abhi','Aryan','Harsh','Rahul','Aman','Rohan','Shardul','Jai','Jeet','Anuj'],
    "Age":[18, 25, 32, 21, 45, 29, 37, 19, 54, 41],
    "Cities":["Delhi","Mumbai","Bengaluru","Chennai","Kolkata","Hyderabad","Pune","Jaipur","Ahmedabad","Chandigarh"]
}
df=pd.DataFrame(data)
print(df)
df.sort_values(by="Age",ascending=False,inplace=True)
print("\n\n-----Sorted by Age-----")
print(df)