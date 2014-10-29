def sqrt(a):
	x=3
	while True:
		y = (x + a/x) / 2
		if abs(y-x)<0.000000000001:
			break
		x = y
	return x
import sys
print sqrt(float(sys.argv[1]))
