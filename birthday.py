from random import randint
def birthday(x):
	i=0
	same=0
	while i<1000:
		if x==str(randint(1,30))+'-'+str(randint(1,12))+'-'+"1992":
			same+=1
		i+=1
	return same
print birthday("7-5-1992")
