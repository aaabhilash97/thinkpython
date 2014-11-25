import os
try:
	fin = open('unique.py')
	for line in fin:
		print line
	fin.close()
except:
	print 'Something went wrong.'
