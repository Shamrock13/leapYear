def leapYear():
    if year % 4 == 0 and year % 400 == 0:
        return True
    else:
        return False
year = int(input())
print (leapYear())
