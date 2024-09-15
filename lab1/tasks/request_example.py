import requests

url = 'https://wttr.in/'
response = requests.get(url)
print(response.text)