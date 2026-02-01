
import pandas as pd
data={
    "Name":['Abhi','Aryan','Anuj','Jai','Jeet','Ayush','Shubham','Aman'],
    "Age":[20,None,19,21,18,21,25,30],
    "Salary":[50000,None,45000,60000,55000,66000,87400,93210],
    "Performance":[90,None,85,80,60,93,86,89]
}

df=pd.DataFrame(data)
print("---Sample data frame---")
print(df)
#linear,polynomial,time
df.interpolate(method="linear")

print(df)