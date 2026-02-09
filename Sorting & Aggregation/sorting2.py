import pandas as pd
data={
    "Name":['Abhi','Aryan','Harsh','Rahul','Aman','Rohan','Shardul','Jai','Jeet','Anuj'],
    "Age":[18, 25, 32, 21, 45, 29, 37, 19, 54, 41],
    "Salary":[28500, 34200, 41750, 52000, 47300, 60800, 38900, 75450, 92100, 120000],
    "Cities":["Delhi","Mumbai","Bengaluru","Chennai","Kolkata","Hyderabad","Pune","Jaipur","Ahmedabad","Chandigarh"]
}
df=pd.DataFrame(data)
print(df)
# print("\n\n---Info of dataframe----")
# print(df.describe())
# print("\n\n-----Sorted by Age-----")
# df.sort_values(by=["Age","Salary"],ascending=[True,False],inplace=True)
# print(df)