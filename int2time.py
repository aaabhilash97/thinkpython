class Time():
	"""time rep"""
def int2time(x):
	t1=Time()
        t1.h=x/3600
        x=x%3600
        t1.m=x/60
        t1.s=x%60
        return t1	
time=int2time(3600)
print time.h,time.m,time.s
