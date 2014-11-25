class Time():
        """time rep"""
def int2time(x):
        t1=Time()
        t1.h=x/3600
        x=x%3600
        t1.m=x/60
        t1.s=x%60
        return t1
def multime(t1,m):
	return int2time(((t1.h*60*60)+(t1.m*60)+(t1.s))*m)
time=Time()
time.h=1
time.m=23
time.s=60
new=multime(time,2)
print new.h,new.m,new.s
