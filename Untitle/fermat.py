def fermat(a,b,c,n):
	if n>2:
		print "Holy Smokes ,Fermat was Wrong"
	elif a**n+b**n==c**n:
		print "yes its fermat"
	else:
		print "No that doesn't work"
fermat(1,1,2,4)
