#!/usr/bin/python3

import urllib.request
import json

MAJORTOM = 'http://api.open-notify.org/astros.json'

def main():

    groundctrl = urllib.request.urlopen(MAJORTOM)

    helmet = groundctrl.read()

    helmetson = json.loads(helmet.decode('utf-8'))

    print('\n\nPeople in space: ', helmetson['number'])
    people = helmetson['people']
   
    for person in people:
        print(person['name'] + ' on the ' + person['craft'])

    


main()
