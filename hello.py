#!/usr/bin/python
import cgitb
import sys
sys.path.append('/var/www/codefortrenton.thefr33.com/cgi-bin/pymongo-3.2.1/build/lib.linux-x86_64-2.7/')
from connection import url
import pymongo

cgitb.enable()

print "Content-Type: text/plain\r\n\r\n"
print
print "Hello World!"

client = pymongo.MongoClient(url)
db = client.trentonbiz
addr= db.addresses
import pprint

for item in addr.find():
    pprint.pprint(item)
    break
