#!/usr/bin/env python3
import requests
from pprint import pprint as pp

## Define APOD 
NASAAPI = 'https://api.nasa.gov/planetary/apod?'
MYKEY = 'api_key=aXllpYgUoDVvvWWD1wovHthmuNbQb7Qz9mL4Offj'    ## your key goes in place of DEMO_KEY

## Call the webservice
nasaapiobj = requests.get(NASAAPI + MYKEY)

## read the file-like object
nasaread = nasaapiobj.json()

print(nasaread)

pp(nasaread)

input('\nThis is pretty print JSON. Press ENTER to continue')

print(nasaread['explanation'], nasaread.get('hdurl', "No HD URL for today"))

