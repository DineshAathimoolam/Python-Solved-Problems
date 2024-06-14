import datetime
mydate=datetime.date(2024,1,1)
print("Date is :",mydate)

tdate=datetime.date.today()
print("Date of today:",tdate)

tdate1=tdate.year
print(tdate1)

#time delta
tdate2=datetime.date.today()
tdelta=datetime.timedelta(days=int(input()))
print(tdate2)
print(tdate2+tdelta)


#time
mytime=datetime.time(10,30,25,12345)
print("The Time is :",mytime.minute)

#No of days passed this year
newyear=datetime.date(2024,1,1)
tdate=datetime.date.today()
print('No of days passed by 2024 is :',(tdate-newyear).days)

