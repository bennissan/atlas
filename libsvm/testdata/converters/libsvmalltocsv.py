from sys import argv
from os import system as call

for i in range(1, len(argv)):
	call("python libsvmtocsv.py %s" % argv[i])