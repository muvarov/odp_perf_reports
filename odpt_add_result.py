#!/usr/bin/python
import json
import pickle
import sys

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

try:
	data = pickle.load( open(fname, "rb" ) )
except:
	data = {}

if name in data:
	tmp = data[name]
	tmp[result] = value
	data[name] =  tmp
else:
	data[name] = {result :value }

json_data = json.dumps(data)

pickle.dump(data, open(fname, "w" ))

print json_data
