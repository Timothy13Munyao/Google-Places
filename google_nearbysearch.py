import json

import requests
from geopy.geocoders import Nominatim
from googleplaces import GooglePlaces

API_KEY = "AIzaSyA_SclUwtLWSmmhx2jx-DYNyR-9dRe6uhE"

# Initialising the GooglePlaces constructor
google_places = GooglePlaces(API_KEY)
geolocator = Nominatim(user_agent='my-application')
loc = input('Enter your location: ')
loc = geolocator.geocode(loc)

print('Your location is: ', loc)
print("Your Latitude is :", loc.latitude, "\nYour Longitude is:", loc.longitude)

lat = loc.latitude
lng = loc.longitude

print()
type = input('What are you looking for (e.g. school, hospital, restaurant, library etc)? ')
print()


def findPlaces(loc=(lat, lng), radius=400, pagetoken=None):
    lat, lng = loc
    url = "https://maps.googleapis.com/maps/api/place/nearbysearch/json?location={lat},{lng}&radius={radius}&type={type}&key={APIKEY}{pagetoken}".format(
        lat=lat, lng=lng, radius=radius, type=type, APIKEY=API_KEY,
        pagetoken="&pagetoken=" + pagetoken if pagetoken else "")
    print(url)
    response = requests.get(url)
    res = json.loads(response.text)
    # print(res)
    print()
    print("***** Your search has yielded: ", len(res["results"]), 'places *****')
    print()

    for result in res["results"]:
        info = "".join(map(str, ['Name: ', result["name"], '\n',
                                 'Latitude: ', result["geometry"]["location"]["lat"], '\n',
                                 'Longitude: ', result["geometry"]["location"]["lng"], '\n',
                                 'Rating: ', result.get("rating", 0), '\n',
                                 'Place ID: ', result["place_id"]]
                           )
                       )
        print(info)
        print('*' * 38)
        print()
    pagetoken = res.get("next_page_token", None)

    print("here -->> ", pagetoken)

    return pagetoken


pagetoken = None

while True:
    pagetoken = findPlaces(pagetoken=pagetoken)
    import time

    time.sleep(10)

    if not pagetoken:
        break
