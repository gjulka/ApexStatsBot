import requests

key = {'TRN-Api-Key': "XXXXXXXXXX-XXXXXXXXXX"}

URL = "https://public-api.tracker.gg/apex/v1/standard/profile/5/ninja"

r = requests.get(url=URL, headers=key)
data = r.json()

lengthOfStatsArray = len(data['data']['stats'])
keys = []

for x in range(0, lengthOfStatsArray):
    statsArray = data['data']['stats'][x]['metadata']['key']
    keys.append(statsArray)

if ("Level") in keys:
    print('YEET')    


