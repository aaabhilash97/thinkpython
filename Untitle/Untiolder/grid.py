def hor(x):
	print '+'+'-'*x+'+'+'-'*(x+1)+'+'
def ver(x):
	i=0
	while (i<x/3):
		print '|'+' '*(x/2)+'|'+' '*(x/2)+'|'+' '*(x/2)+'|'+' '*(x/2)+'|'
		i=i+1
	hor(x)
def grid(x):
	hor(x)
	ver(x)
	ver(x)
	ver(x)
	ver(x)
grid(4)
