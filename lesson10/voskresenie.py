days_in_months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

def day_of_week(year, month, day):
    '''
    Return the day of the week, Monday is 1 and Sunday is 7.
    1.01.1900 is Monday
    '''
    return num_days(year, month, day) % 7 or 7


def num_days(year, month, day):
    '''
    Return number days between 1.01.1900 and year, month, day
    '''
    # add days
    num = day
    # iterate years
    for y in range(1900, year):
        num += 365
        if is_leap(y):
            num += 1
    # iterate months
    for m in range(1, month):
        num += days_in_months[m-1]
        if m == 2 and is_leap(year):
            num += 1
    return num


def is_leap(year):
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)


def num_sundays(start_year, end_year):
    num = 0
    for year in range(start_year, end_year + 1):
        for month in range(1, 13):
            if day_of_week(year, month, 1) == 7:
                num += 1
    return num


print(num_sundays(1901, 2000))
