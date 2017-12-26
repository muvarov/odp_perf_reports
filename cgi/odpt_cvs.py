#!/usr/bin/python
import json
import pickle
import sys
import datetime
import time
import cgi

fname = "odpt_all_results.dat"

def utc_time_to_date(utime):
        d = datetime.datetime.fromtimestamp(utime).strftime('%c')
        return d

try:
	data = pickle.load( open(fname, "rb" ) )
except:
	data = []


qin = sys.stdin.read()

print("Content-type: text/csv\n")

print "time,",
print "commit,",
print "author,",
print "RX,",
print "TX"

for r in data:
	print utc_time_to_date(r["time"]),",",
	print r["commit"],",",
	print r["author"],",",
	RX=0
	TX=0
	for res in r["results"]:
		if "generator" in res:
			generator = res["generator"]
			if "RX" in generator:
				RX = generator["RX"]
			elif "TX" in generator:
				TX = generator["TX"]
	print RX,",",
	print TX,
