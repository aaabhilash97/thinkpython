from random import randint
def gcd(a,b):
	prime=[]
	for  i in range(a,b):
		for k in range(2,i):
			if i%k==0:
				cond=False
				break
			else:
				cond=True
		if cond==True:
			prime.append(i)
	return prime
def gcd1(a,b):
        if a%b==0:
                return b
        return gcd(b,a%b)

def rsaencryption(m,ed):
	p=3
	q=11
	n=p*q
	phin=(p-1)*(q-1)
	for e in gcd(3,phin):
		if n%e==0:
			print ""
		else:
		#	print "e ok",e
			break
	for d in range(2,10000):
		if d*e==1%phin:
		#	print "d ok",d
			break
	pub=(e,n)
	priv=(d,n)
	print pub,priv
	if ed=="e":
		return (m**d)%33
	if ed=="d":
		return (m**e)%33
print rsaencryption(101,"e")
print rsaencryption(rsaencryption(101,"e"),"d")
