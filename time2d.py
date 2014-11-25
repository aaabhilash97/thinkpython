class Time(object):
	h=2
	m=0
	s=2
def print_time(Time):
	print '%.2d:%.2d:%.2d' %(Time.h,Time.m,Time.s)
time=Time()
print_time(time)
