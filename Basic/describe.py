#step 1 sample data frame

import pandas as pd
data={
    "Name":['Abhi','Aryan','Anuj','Jai','Jeet','Ayush','Shubham','Aman'],
    "Age":[20,17,19,21,18,21,25,30],
    "Salary":[50000,40000,45000,60000,55000,66000,87400,93210],
    "Performance":[90,97,85,80,60,93,86,89]
}

df=pd.DataFrame(data)
print("Sample data frame")
print(df)

print("Descriptive Statistics")
print(df.describe())