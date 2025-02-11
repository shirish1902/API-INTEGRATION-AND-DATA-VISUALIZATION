import requests
import matplotlib.pyplot as plt
from datetime import datetime, timedelta

API_KEY = "019bd3a6c8375fedb6dc682d1bdf77dd"
CITY = "London"
BASE_URL = "http://api.openweathermap.org/data/2.5/forecast"


params = {
    "q": CITY,
    "appid": API_KEY,
    "units": "metric"
}

response = requests.get(BASE_URL, params=params)
data = response.json()


if data.get('cod') != '200':
    print(f"Error: {data.get('cod')} - {data.get('message')}")
    print(f"Full API response: {data}")
    exit()

timestamps = []
temperatures = []
humidity_values = []


if 'list' in data:
    for item in data['list'][:8]:
        timestamp = datetime.fromtimestamp(item['dt'])
        timestamps.append(timestamp)
        temperatures.append(item['main']['temp'])
        humidity_values.append(item['main']['humidity'])
else:
    print("Error: 'list' key not found in API response. Check the API documentation and your request parameters.")
    exit()

plt.figure(figsize=(12, 6))

# Temperature plot
plt.subplot(2, 1, 1)
plt.plot(timestamps, temperatures, marker='o', linestyle='-', color='red')
plt.title(f"Temperature Forecast for {CITY}")
plt.ylabel("Temperature (°C)")
plt.xticks(rotation=45)

# Humidity plot
plt.subplot(2, 1, 2)
plt.bar(timestamps, humidity_values, color='blue', alpha=0.7)
plt.title(f"Humidity Forecast for {CITY}")
plt.ylabel("Humidity (%)")
plt.xticks(rotation=45)

plt.tight_layout()
plt.savefig("weather_dashboard.png")
plt.close()

print(f"Weather dashboard for {CITY} has been saved as 'weather_dashboard.png'")
