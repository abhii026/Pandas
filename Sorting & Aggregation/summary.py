#  df["Column_name"].mean()
#  df["Column_name"].sum()
#  df["Column_name"].min()
#  df["Column_name"].max()
import pandas as pd
data={
    "Name":['Abhi','Aryan','Harsh','Rahul','Aman','Rohan','Shardul','Jai','Jeet','Anuj'],
    "Age":[18, 25, 32, 21, 45, 29, 37, 19, 54, 41],
    "Salary":[28500, 34200, 41750, 52000, 47300, 60800, 38900, 75450, 92100, 120000],
    "Cities":["Delhi","Mumbai","Bengaluru","Chennai","Kolkata","Hyderabad","Pune","Jaipur","Ahmedabad","Chandigarh"]
}
df=pd.DataFrame(data)
print(df)

min=df["Salary"].min()
print(f"\nMinimum Salary is {min}")
max=df["Salary"].max()
print(f"Maximum Salary is {max}")
sum=df["Salary"].sum()
print(f"Sum of Salary is {sum}")
average=df["Salary"].mean()
print(f"Average Salary is {average}")