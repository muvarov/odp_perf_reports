#!/usr/bin/python
import json
import pickle
import sys
import urllib2
import datetime

url = sys.argv[1]
git_commit = sys.argv[2]
author = sys.argv[3]

fname = "odpt_results.dat"

def get_utc_time():
	d = datetime.datetime.utcnow()
	epoch = datetime.datetime(1970,1,1)
	t = (d - epoch).total_seconds()
	return t

d = pickle.load( open(fname, "rb" ) )
data = {"time" : get_utc_time(),
	"commit" : git_commit,
	"author" : author,
	"results" : d }


req = urllib2.Request(url)
req.add_header('Content-Type','application/json')

js = json.dumps(data)

print urllib2.urlopen(req, js).read()
