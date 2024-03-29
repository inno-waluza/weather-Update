import requests
from locapi import latitude
from locapi import longtude

api_key = "a363d903acb231f2b6edf46912e254bf"
#lat and lon from locapi
lat = latitude
lon = longtude
weather_data = requests.get(f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={api_key}&units=metric")
api_response = weather_data.json() 

if weather_data.json()['cod'] == '404':
        print("No City Found")
elif weather_data.json()['cod'] == '401' :
        print("Invalid API key")  
else:     
        #extracting Data
        weather = weather_data.json()['weather'][0]['description']
        temp = round(weather_data.json()['main']['temp'])
        humidity = round(weather_data.json()['main']['humidity'])
        wind_speed = round(weather_data.json()['wind']['speed'])
        visibility = round(weather_data.json()['visibility'])

        print(weather)
        print("temperature: ", temp , "degrees celcius")
        print("humidity: ", humidity, "%")
        print("wind speed: ", wind_speed, "Km/hr")
        print("Visibility: ", visibility, "m")