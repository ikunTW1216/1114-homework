def  get_start_day(year, month):
    if month == 1 or month == 2:
        year = year -1
    
    day = (1 + (13*(month+1))/5 + int(year%100) + (int(year%100)/4) + ((year//100)/4) + (5*(year//100)))%7

    return int((day+5)%7)
        

print(get_start_day(2024, 11))