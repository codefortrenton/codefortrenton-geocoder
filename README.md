# codefortrenton-geocoder

## Create the indexes

    mongo code_for_trenton
    db.addresses.ensureIndex( { Name :1 }, { unique:true, dropDups:true})
    db.addresses.createIndex( { Name: 1 }, { unique: true } )

## Keys

secrets.py contains

    opencage_key = 'XXXX'

create it here https://geocoder.opencagedata.com/

## need libs

Using pymongodb

and MongoDB version: 2.4.14

Locally checked out python-opencage-geocoder

    git clone git@github.com:OpenCageData/python-opencage-geocoder.git


## Data is from fusion table to start with 

    https://www.google.com/fusiontables/exporttable?query=select+*+from+1L7eDqaZi9F5ZszM_URjC7k48mKLTZen1iWdChHon&o=csv

For shell access to this, see : https://fusion-tables-api-samples.googlecode.com/svn/trunk/ftapi/README.html


# Export

    mongoexport -d code_for_trenton -c addresses > addresses.json
    bzip2 addresses.json 


# Geocoding of sms :

1. using google voice to email trello
2. trello as ticket storage
3. using nltk to parse out text.
4. using opencage for geocoding
5. storing of geocode in ticket
