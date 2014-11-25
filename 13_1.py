from string import *
def line2words(x):
	f=open(x).read().split()
	i=0
	while i<len(f):
	    f[i]=f[i]+"\n"
	    for p in punctuation:
		f[i]=lower(f[i])
		f[i]=replace(f[i],p,"")
	    i+=1
	print f
	fle=open(x,'w')
	fle.writelines(f)
line2words("word.txt")

