import requests
from ipFounder import ip
from ipFounder import api_key
##gets current user public ip
ip_now = ip
##making http request
data = requests.get(f"https://api.ipgeolocation.io/ipgeo?apiKey={api_key}&ip={ip_now}")
response = data.json()
latitude = response['latitude']
longtude = response['longitude']
##print(response)
#print(response.keys())
#print(response['calling_code'])