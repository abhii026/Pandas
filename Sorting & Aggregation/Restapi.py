import pandas as pd
import requests
API_KEY="5709468af9031f12fafcbb3ed59d1189"
BASE_URL="http://api.openweathermap.org/data/2.5/weather"

params={
    "q":"Delhi",
    "appid":API_KEY,
    "units":"metric"
}
response=requests.get(BASE_URL, params=params)
print("Status Code:",response.status_code)
print("Raw Response",response.text)
if response.status_code==200 and response.text.strip():
    data=response.json()
    # print(data)
else:
    print("Failed to fetch JSON data")

print(data.keys())
weather_data={
    "city":data["main"]["temp"],
    "humidity":data["main"]["humidity"],
    "pressure":data["main"]["pressure"],
    "wind_speed":data["wind"]["speed"],
    "weather":data["weather"][0]["description"]
}
print(weather_data)
df=pd.DataFrame([weather_data])
print("\n\n\n----Data frames----")
print(df)
df.to_csv("weather_data.csv",index=False)