# '''
# 1- How big is your dataset
# 2- What are name of columns
# '''
# shape it is attributes it return tuple woth two values (no. of rows and no.of column)
#columns it returns name columns

import pandas as pd
data={
    "Name":['Abhi','Aryan','Anuj','Jai','Jeet','Ayush','Shubham','Aman'],
    "Age":[20,17,19,21,18,21,25,30],
    "Salary":[50000,40000,45000,60000,55000,66000,87400,93210],
    "Performance":[90,97,85,80,60,93,86,89]
}
df=pd.DataFrame(data)
# print(f'Shape: {df.shape}')
# print(f'Columns: {df.columns}')


#select specific column- using square bracket
# a series and dataframes multiple columns of data
# column=df["Column Name"]
#subset=df["Column1","Column2","..."]

# print(f"Names (Single column return series): {df["Name"]}")
# print(f"Names (Multiple columns return dataframes): {df[["Name","Age"]]}")

#filter rows- boolean (indexing)
# filtered_Rows=df[df["Salary"]>5000]
# filtered_Rows=df[(df["Salary"]>50000) &(df["Column2"]<80000)]


# high_salary=df[df["Salary"]>50000]
# print(f"Employes with more then 50000 salary is {high_salary}")

between_sal=df[(df["Salary"]>50000) & (df["Salary"]<80000)]
print(f"Employes with more then 50000 salary and less then 80000 is {between_sal}")

#combine multiple conditions