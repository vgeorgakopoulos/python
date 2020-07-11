import requests
import json
url = 'https://api.darksky.net/forecast/04c68ff0bcc56159c67f870ac2a47f62/42.3601,-71.0589'
url2 = 'http://api.open-notify.org/iss-pass.json'
'''
key='04c68ff0bcc56159c67f870ac2a47f62'
parameters = {
    "latitude": 42.3601,
    "longitude": -71.0589
}
'''
#response=requests.get(url)

parameters = {
    "lat": 42.3601,
    "lon": -71.0589
}
response=requests.get(url2, params=parameters)
#response=requests.get(url)
print('---------------------------------------------------------------------------------------------\n')
print('API response:', response.status_code)
print('---------------------------------------------------------------------------------------------\n')
print('URL API call:', response.url)
print('---------------------------------------------------------------------------------------------\n')
print('response.json() returns an object of type:', type(response.json()))
print('---------------------------------------------------------------------------------------------\n')
print(response.json())
result_dict=response.json()
for keys in result_dict:
    print('---------------------------------------------------------------------------------------------\n'
    ,keys, result_dict[keys], '\n')
print(response.raw)








