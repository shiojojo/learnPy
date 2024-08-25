import calendar  

class MyCalendar(calendar.Calendar):
    def __init__(self):
        super().__init__()

    def count_weekday_in_year(self,year,weekday):
        count_weekday = 0

        for i in range(1,13):
            for data in self.monthdays2calendar(year, i):
                if data[weekday][0] != 0:
                    count_weekday += 1
        return count_weekday

myc = MyCalendar()
print(myc.count_weekday_in_year(year=2019, weekday=0))
print(myc.count_weekday_in_year(year=2000, weekday=6))
