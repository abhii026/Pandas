import pandas as pd

#how to know how many row
#using head() and tail()
#head() tail() by deafult 5 row
#head(n)  starting n rows
#tail(n)  last n rows
df=pd.read_csv(r"C:\Users\iabhi\OneDrive\Desktop\DataScience_Python\datasets\diabetes.csv")
print("Display 10 rows of starting")
print(df.head(10))
print("Display 10 rows of last")
print(df.tail(10))
 