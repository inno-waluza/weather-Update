from requests import get

ip = get('https://api.ipify.org').text
##print(ip)
pub_ip = ('My public IP address is: {}'.format(ip))
api_key = 'ce884ea38f0c41d3b9fef968fdaaf502'