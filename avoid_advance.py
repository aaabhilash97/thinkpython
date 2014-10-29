import string
def avoid(x):
	f=x.split()
	print f
        for w in f:
                for w1 in w:
			if w1 not in string.punctuation:
				cond=True
			else:
				cond=False
				break
		if cond==True:
			print w
i=raw_input("entr file")
avoid(i)

