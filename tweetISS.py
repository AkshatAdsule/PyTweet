import requests
from datetime import datetime
from opencage.geocoder import OpenCageGeocode

key = 'a00614947d4d49eebe9a0e5e919f973a'

geocoder = OpenCageGeocode(key)

input = input("Enter a city or adress to find when the ISS will go over you: ")
query = input
results = geocoder.geocode(query)

output = (u'%f;%f;%s;%s' % (results[0]['geometry']['lat'], 
                        results[0]['geometry']['lng'],
                        results[0]['components']['country_code'],
                        results[0]['annotations']['timezone']['name']))

print (output)
outputstr = str(output)
outputstr = output.split(";")
cityout = outputstr[3]

parameters = {
    "lat": outputstr[0],
    "lon": outputstr[1] }

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
    print("The ISS will be over ", input, " on ", time)
    #print(time)