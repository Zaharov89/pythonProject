year = int(input("Введите год:"))
def is_year_leap(year):
    if (year % 4 == 0):
        print("год", year,":", "True")
    else:
        print("год", year,":", "False")

year2 = is_year_leap(year)

