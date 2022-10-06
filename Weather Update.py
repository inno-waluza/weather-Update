
from operator import truediv
import requests
while True:
    city = input("Enter City Name: ")
    api_key = '30d4741c779ba94c470ca1f63045390a'
    weather_data = requests.get(
    f"https://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&APPID={api_key}")
    api_response = weather_data.json() 
  
    #print(api_response) 
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

       #display weather data
    print("Weather in " + city)
    print()
    print("weather is ",weather)
    print("The Temperature is" ,temp ,"ºC")
    print("humidity is " ,humidity, "%")
    print("Wind speed is " ,wind_speed)
    print("Visibility is ",visibility,"m")