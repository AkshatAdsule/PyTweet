import requests

r = requests.get('https://icanhazdadjoke.com/')
print(r.json)