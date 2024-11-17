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

if __name__ == '__main__':
    print(is_leap_year(2000))