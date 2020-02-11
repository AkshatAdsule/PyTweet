import requests
from datetime import datetime

parameters = {
    "lat": 37.3229978,
    "lon": -122.0321823 }

response = requests.get("http://api.open-notify.org/iss-pass.json", params=parameters)
pass_times = response.json()['response']
#print(pass_times)
risetimes = []

for d in pass_times:
    time = d['risetime']
    risetimes.append(time)
times = []

for rt in risetimes:
    time = datetime.fromtimestamp(rt)
    times.append(time)
    print("The ISS will be over you on ", time)
    #print(time)