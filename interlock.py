def interlock(x):
	s=[]
	s.append(x)
	s.append(x[::2])
	s.append(x[1::2])
	return s
print interlock("abhilash")
