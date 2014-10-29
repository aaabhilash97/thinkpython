import string
def avoid(x):
	f=open(x).read().split()
	f="".join(f)
	for w in f:
		if w in string.punctuation:
			return False
	return True
i=raw_input("entr file")
print avoid(i)	
