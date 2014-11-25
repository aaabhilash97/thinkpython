import copy
class Time(object):
        h=5
        m=0
        s=0
def pureinc(t,s):
	t1=copy.copy(t)
        x=(t1.h*60*60)+(t1.m*60)+(t1.s)+s
        t1.h=x/3600
        x=x%3600
        t1.m=x/60
        t1.s=x%60
	return t1
time=Time()
new=pureinc(time,60)
print new.h,':',new.m,':',new.s

