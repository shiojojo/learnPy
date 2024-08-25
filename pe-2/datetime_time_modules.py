import datetime

dt = datetime.datetime(year=2020, month=11, day=4, hour=14, minute=53, second=00)

print(dt.strftime("%Y/%m/%d %H:%M:%S"))
print(dt.strftime("%y/%B/%d %H:%M:%S %p"))
print(dt.strftime("%a, %Y %b %d"))
print(dt.strftime("%A, %Y %B %d"))
print("Weekday: " + str(dt.isoweekday()))
print("Day of the year: " + dt.strftime("%j"))
print("Week number of the year: " + dt.strftime("%U"))

# 2020/11/04 14:53:00
# 20/November/04 14:53:00 PM
# Wed, 2020 Nov 04
# Wednesday, 2020 November 04
# Weekday: 3
# Day of the year: 309
# Week number of the year: 44