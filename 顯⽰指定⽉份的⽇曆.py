def is_leap_year(year): #判斷閏、平年
    if year%400 == 0:
        return  True
    elif year%4 == 0:
        if year%100 == 0:
            return False
        else:
            return True
    else:
        return False

def get_days_in_month(year, month): #判斷天數
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

def  get_start_day(year, month): #判斷每月1號是禮拜幾
    if month == 1 or month == 2:
        year = year -1
        if year == 1:
            month += 1
        else:
            month += 2
    
    day = (1 + (13*(month+1))/5 + int(year%100) + (int(year%100)/4) + ((year//100)/4) + (5*(year//100)))%7

    return int((day+5)%7)

def display_calendar(year, month): #印出日曆
    
    print(f'   {year}年 {month}月')
    print('Mo Tu We Th Fr Sa Su')
    
    for i in range(get_start_day(year, month)):
        print('  ', end=' ')
        
    for i in range(1, get_days_in_month(year, month)+1):
        if (i+1)%7==0:
            print()
            
        print('%2s' %(i), end=' ')


display_calendar(2023, 11)