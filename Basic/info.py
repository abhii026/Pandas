import pandas as pd

# df=pd.read_csv(r"C:\Users\iabhi\OneDrive\Desktop\DataScience_Python\datasets\diabetes.csv")
data={
    "Name":['Abhi','Jeet','Jai'],
    "Age":[20,22,21],
}
df=pd.DataFrame(data)
print("Displaying the info of data set")
print(df.info())