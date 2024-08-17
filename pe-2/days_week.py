class WeekDayError(Exception):
    pass
	

class Weeker:
    week = ("Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun")

    def __init__(self, day):
        if day not in Weeker.week:
            raise WeekDayError
        else:
            self.__day = day

    def __str__(self):
        return self.__day

    def add_days(self, n):
        self.__day = self.week[(self.week.index(self.__day) + n) % 7]

    def subtract_days(self, n):
        self.__day = self.week[(self.week.index(self.__day) - n) % 7]


try:
    weekday = Weeker('Mon')
    print(weekday)
    weekday.add_days(15)
    print(weekday)
    weekday.subtract_days(23)
    print(weekday)
    weekday = Weeker('Monday')
except WeekDayError:
    print("Sorry, I can't serve your request.")
