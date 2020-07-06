
# You are given the following information, but you may prefer to do some research for yourself.

# 1 Jan 1900 was a Monday.
# Thirty days has September,
# April, June and November.
# All the rest have thirty-one,
# Saving February alone,
# Which has twenty-eight, rain or shine.
# And on leap years, twenty-nine.
# A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.
# How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?


def reset_week(days):
    days = 0 if days > 5 else days + 1
    return days

def get_days_count_in_month(year, month):
    if month == 1:
        if not (year + 1900) % 4:
            if not (year + 1900) % 100 and (year + 1900) % 400:
                return 28
            else:
                return 29
        else:
            return 28
    if month in (3, 5, 8, 10):
        return 30
    return 31
    
def get_sundays():
    years = 30
    months = 0
    days = 0
    day_of_week = 1
    sundays_count = 0
    for years in range(0, 101):
        for months in range(12):
            for days in range(get_days_count_in_month(years, months)):
                if days == 0 and day_of_week == 0 and years > 0:
                    sundays_count += 1
                day_of_week = reset_week(day_of_week)
            days = 0
        months = 0
    return sundays_count

print(get_sundays())
