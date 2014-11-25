import random
class Time(object):
	h=random.randint(0,24)
	m=random.randint(0,60)
	s=random.randint(0,60)
def chrono(t1,t2):
	x=(t1.h*60*60)+(t1.m*60)+(t1.s)
	y=(t2.h*60*60)+(t2.m*60)+(t2.s)
	return x<y
t1=Time()
t2=Time()
t1.h=12
t2.h=22
print chrono(t1,t2)
