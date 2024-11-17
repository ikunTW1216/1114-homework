def is_leap_year(year):
    if year%400 == 0:
        return  True
    elif year%4 == 0:
        if year%100 == 0:
            return False
        else:
            return True
    else:
        return False

def get_days_in_month(year, month):
    X = [4, 6, 9, 11]
    
    if month == 2:
        if is_leap_year(year):
            return 29
        else:
            return 28
        
    elif month in X:
        return 30
    
    else:
        return 31
    
print(get_days_in_month(2021, 12))
