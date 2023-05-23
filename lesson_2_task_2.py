year = int(input("Введите год:"))
def is_year_leap(year):
    if (year % 4 == 0):
        return True
    else:
        return False

year2 = is_year_leap(year)

if (year2 == True):
    print("год", year,":", "True")
else:
    print("год", year,":", "False")
