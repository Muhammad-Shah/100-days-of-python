# Days in Month

def is_leap(c_year):
    if c_year % 4 == 0:
        if c_year % 100 == 0:
            if c_year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False

def days_in_months(p_year, p_month):
    days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    
    if is_leap(c_year=p_year) and p_month == 2:
        return 29
    return days_in_month[p_month-1]


# Taking Inputs
year = int(input("Enter a year: "))
month = int(input("Enter a month: "))
days = days_in_months(year, month)
print(days)