def is_leap(year: int):
    """
    Returns true if it is a leap year, otherwise false
    """
    return year % 4 == 0 and ((year % 100 != 0) or (year % 100 == 0 and year % 400 == 0))


def days_in_month(year: int, month: int):
    """
    Year and month input, returns number of days in a month in a specific year
    """
    if month == 2 and is_leap(year):
        return 29
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    return month_days[month - 1]


# 🚨 Do NOT change any of the code below
year = int(input("Enter a year: "))
month = int(input("Enter a month: "))
days = days_in_month(year, month)
print(days)












