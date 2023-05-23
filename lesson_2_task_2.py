year = input("Введите год:")
year2 = int(year)
def is_year_leap(year2):
    if (year2 % 4 == 0):
        print(True)
    else:
        print(False)

year3 = is_year_leap(year2)
print(year3)

if (year3 == True):
    print("год", year,":", "True")
else:
    print("год", year,":", "False")
