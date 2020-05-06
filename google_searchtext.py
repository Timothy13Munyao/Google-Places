"""
Python program to get a set of places according to your search query using Google Places API
"""

# importing required modules
import requests
from googleplaces import GooglePlaces

# enter your api key here
api_key = 'API_KEY'

# Initialising the GooglePlaces constructor
google_places = GooglePlaces(api_key)

# url variable store url
url = "https://maps.googleapis.com/maps/api/place/textsearch/json?"

# The text string on which to search
print()
print('Example search query: Schools in Thika, Hospitals in Makueni, Restaurants in Mombasa etc')
print()
query = input('What and where are you looking for?: ')
print()
print('-' * 50, '\n')
print('Here is your search results...', '\n')

# get method of requests module return response object
r = requests.get(url + 'query=' + query +
                 '&key=' + api_key)

# json method of response object convert json format data into python format data
x = r.json()
"""
now x contains list of nested dictionaries
we know dictionary contain key value pair
store the value of result key in variable y
"""
y = x['results']

# keep looping upto length of y
for i in range(len(y)):
    # Print value corresponding to the 'name' key at the ith index of y
    print('STATUS:', y[i]['business_status'])
    print('COORDINATES:', y[i]['geometry'].get('location'))
    print('ADDRESS:', y[i]['formatted_address'])
    print('NAME:', y[i]['name'], '\n')

print()
