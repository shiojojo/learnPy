def is_year_leap(year):
    if year < 1582:
        return None
    if year % 4 != 0 or (year % 100 == 0 and year % 400 != 0):
        return False
    else:
        return True

def days_in_month(year, month):
    if (year == 1582 and month < 10) or is_year_leap(year) == None:
        return None
    if month == 2:
        if is_year_leap(year):
            return 29
        else:
            return 28
    elif month in [4,6,9,11]:
        return 30
    elif month in [1,3,5,7,8,9,10,12]:
        return 31
    else:
        return None

def day_of_year(year, month, day):
    if year == 1582:
        return None
        
    check_days = days_in_month(year, month)
    if check_days == None:
        return None
    if day <= 0 or day > check_days:
        return None
    for i in range(1,month):
        day += days_in_month(year, i)     
    return day

print(day_of_year(1582, 12, 21))
print(day_of_year(2002, 7, 21))
