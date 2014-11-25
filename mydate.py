class Date(object):
	y=1947
	m=8
	d=15
date=Date()
def date2days(date):
	i=1
	days=date.d
	while i<=date.m:		
		if i%2==1 and i is not 2:
			days+=31
		elif i%2==0 and i is not 2:
			days+=30
		elif i==2:
			if date.y%4==0:
				days+=29
			else:
				days+=28
		i+=1
	return days
def days2date(days,year):
	date=Date()
	i=1
	dm=31
	while days>dm:
		if i==2:
			if year%4==0:
				days-=29
			else:
				days-=28
		elif i%2==1:
			days-=31
		else:
			days-=30
		i+=1
		if i>12:
			year+=1
			i=1
		if i==2 and year%4==0:
			dm=29
		elif i==2 and year%4 is not 0:
			dm=28
		else:
			if i%2==1:
				dm=31
			elif i%2==0:
				dm=30
	date.y=year
	date.m=i-1
	date.d=days
	return date
def incdate(date,n):
	days=date2days(date)+n
	return days2date(days,date.y)
d=incdate(date,356)
print d.y,d.m,d.d
