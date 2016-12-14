#!/usr/bin/env python
import re
import sys

for line in sys.stdin:
	# remove leading and trailing whitespace
	val = line.strip()
	# extract values from line
	(year, temp, q) = (val[15:19], val[87:92], val[92:93])
	# print year and temp if valid temperature
	if (temp != "+9999" and re.match("[01459]", q)):
		print "%s\t%s" % (year, temp)