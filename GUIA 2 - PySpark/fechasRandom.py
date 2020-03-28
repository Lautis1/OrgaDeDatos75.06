import random 
import time
import datetime

def str_time_prop(start, end, format, prop):
	"""Get a time at a proportion of a range of two formatted times.
	start and end should be strings specifying times formated in the given format (strftime-style), giving an interval [start, end]. popr specififies how a proportion of the interval to be taken after start. The returned time will be in the specifified format."""

	stime = time.mktime(time.strptime(start,format))
	etime = time.mktime(time.strptime(end, format))

	ptime = stime + prop * (etime - stime)

	return time.strftime(format, time.localtime(ptime))

def random_date(start, end):
	return str_time_prop(start, end, '%Y-%m-%d', random.random())