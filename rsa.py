from random import randint,choice
def gcd(a,b):
	prime=[]
	cond=False
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
#RSA ENCRYPTION
def rsaencryption(m,ed):
	p=choice(gcd(33,151))
	q=choice(gcd(33,151))
	n=p*q
	phin=(p-1)*(q-1)
	for e in gcd(2,phin):
		if phin%e==0:
			e=None
		else:
			break
	cond=False
	for d in range(1,1000000):
		for k in range(1,10000):
			if d*e==1+k*phin:
				cond=True
				break
		if cond==True:
			break
	pub=(e,n)
	priv=(d,n)
	return [(m**e)%n,priv]
#RSA DECRYPTION
def rsadecryption(x):
	return x[0]**x[1][0]%x[1][1]
encmsg=rsaencryption(11,"e")
print encmsg
print rsadecryption(encmsg)
