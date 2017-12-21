#!/usr/bin/python
import json
import pickle
import sys
import datetime

def usage():
	print "Script to add test result in odpt_results.dat"
	print "Usage %s test_name field value" % sys.argv[0]
	print "Example: %s generator RX 1000" % sys.argv[0]

if len(sys.argv) != 4:
	usage()
	sys.exit(-1)

name = sys.argv[1]
result = sys.argv[2]
value = sys.argv[3]

fname = "odpt_results.dat"

def get_utc_time():
	d = datetime.datetime.utcnow()
	epoch = datetime.datetime(1970,1,1)
	t = (d - epoch).total_seconds()
	return t

try:
	data = pickle.load( open(fname, "rb" ) )
except:
	data = []

newdata = {}

tmp = {}
tmp[result] = value
tmp["time"] = get_utc_time()
newdata[name] = tmp

data.append(newdata)

json_data = json.dumps(data)

pickle.dump(data, open(fname, "w" ))

print json_data
