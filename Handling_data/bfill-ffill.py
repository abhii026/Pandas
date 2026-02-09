import pandas as pd

df = pd.DataFrame({
    "Temp": [30, None, None, 33, None]
})

df["Temp_bfill"] = df["Temp"].bfill()
print("bfill")
print(df)
df["Temp_ffill"] = df["Temp"].ffill()
print("ffill")
print(df)
