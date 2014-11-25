from pronounce import *
def homophone(x):
	l=read_dictionary()
	for k,v in l.items():
		if l[x]==v:
			print k
import sys
homophone(sys.argv[1])
