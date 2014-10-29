from math import sqrt,factorial
def eval_pi():
	pi=0
	k=0
	while True:
		t=(2*sqrt(2)*factorial(4*k)*(1103+26390*k))/(9801*((factorial(k))**4)*(396)**(4*k))
		if abs(t)<0.00000000000000001:
			return 1/pi
		pi=pi+t
		k=k+1
print eval_pi()
