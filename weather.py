import requests

city = "Bengaluru"
api_key = "your_api_key_here"

url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

response = requests.get(url)
data = response.json()

print("City:", city)
print("Temperature:", data['main']['temp'], "°C")
print("Weather:", data['weather'][0]['description'])