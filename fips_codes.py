import requests
import urllib


lats = dataframe.latitude
lons = dataframe.longitude

iteration = 0
fips_codes = []

# iterate through df, query census api for FIPS code, append to df row
for location in lats:
    lat, lon = lats[iteration], lons[iteration]
    try:
        #Encode parameters 
        params = urllib.parse.urlencode({'latitude': lat, 'longitude':lon, 'format':'json'})
        #Contruct request URL
        url = 'https://geo.fcc.gov/api/census/block/find?' + params

        #Get response from API
        response = requests.get(url)

        #Parse json in response
        data = response.json()

        #append to list
        fips_codes.append(data['County']['FIPS'])
        iteration = iteration + 1
    except:
        pass