import pandas as pd

data={
    "Time":[1,2,3,4,5],
    "value":[10,None,30,None,50]
}
df=pd.DataFrame(data)
print("-----Before Interpolation-----")
print(df)
df['value']=df['value'].interpolate(method="linear")
print("\n-----Before Interpolation-----")
print(df)


"""
1- time series data
2- numeric data with trends
3- avoid dropping rows

"""