#!/usr/bin/python
# Import required libraries

from __future__ import division
import sys
"""
documentation!
"""
# Start a counter and store the textfile in memory
age = 0
count = 0
impressions = 0
lines = sys.stdin.readlines()
lines.pop(0)
n = len(lines)

# For each line, find the sum of index 2 in the list.
for line in lines:
	clean_line = line.strip().split(',')
  	age = age + int(clean_line[0])

 	impressions = impressions + int(clean_line[2])
 

print 'Total Unique Visitors: ', n
print "Total Impressions: ", impressions
print "Average Age: ", age/n
