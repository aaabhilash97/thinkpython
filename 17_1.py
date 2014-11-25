class Time(object):
	def timetoint(t1):
        	return (t1.h*60*60)+(t1.m*60)+(t1.s)
time=Time()
time.h=3
time.m=9
time.s=0
print Time.timetoint(time)

