import requests, json

api_key = "da5a76c2ac3de6cedfd2bf5f986d063e"

base_url = "http://api.openweathermap.org/data/2.5/weather?"

city_name = input("Enter your city name : ")

complete_url = base_url + "appid=" + api_key + "&q=" + city_name

response = requests.get(complete_url)

x = response.json();

if x["cod"] != "404":
    y = x["main"]
    current_temperture = y["temp"]
    current_pressure = y["pressure"]
    current_humidity = y["humidity"]
    z = x["weather"]
    weather_description = z[0]["description"]

    print("Temperature (in Kelvin) = " +str(current_temperture)+"\n Atmospheric Pressure (in hPa) = " + str(current_pressure) + "\n Humidity (in Percentage) = " +str(current_humidity)+ "\n Description = " +str(weather_description))

else:
    print("City Not Found !!")