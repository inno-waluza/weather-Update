import requests
from Ipfounder import ip
from Ipfounder import api_key
##gets current user public ip
ip_now = ip
##making http request
data = requests.get(f"https://api.ipgeolocation.io/ipgeo?apiKey={api_key}&ip={ip_now}")
response = data.json()
latitude = response['latitude']
longtude = response['longitude']
