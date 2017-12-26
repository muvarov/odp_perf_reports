#!/usr/bin/python

import cgi
import pickle
import sys
import time
import json
from StringIO import StringIO
import sys, urllib
from cgi import parse_qs, escape
import re

import datetime
from pymongo import MongoClient
import pprint

qin = sys.stdin.read()

print("Content-type: text/html\n")
print("""<!DOCTYPE HTML>
        <html>
        <head>
            <meta charset="utf-8">
            <title>some title</title>
        </head>
        <body>""")

import urllib
import urlparse
print "Sever got", qin

io = StringIO(qin)
js = json.load(io)

fname = "odpt_all_results.dat"

try:
        data = pickle.load( open(fname, "rb" ) )
except:
        data = []


data.append(js)

pickle.dump(data, open(fname, "w" ))

#print "All data:", data

#client = MongoClient('mongodb://localhost:27017/')
#db = client['test-database']


#posts = db.posts
#post_id = posts.insert_one(js).inserted_id


#dump all
#for post in posts.find():
#	pprint.pprint(post)

print("<h1>all ok!</h1>")
print("</body></html>")
