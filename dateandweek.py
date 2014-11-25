import datetime
d=datetime.date.today()
print "Date:-",d.isoformat()
print "WeekOfDay:-",datetime.date(d.year,d.month,d.day).weekday()
