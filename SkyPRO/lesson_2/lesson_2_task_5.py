#month = ["Декабрь", "Январь", "Февраль", "Март", "Апрель", "Май", "Июнь", "Июль", "Август", "Сентябрь", "Октябрь", "Ноябрь"]

#winter = month[0: 3]
#spring = month[3: 6]
#summer = month[6: 9]
#autumn = month[9: 12]

# Список выше был лишним. Ничего не придумал, что с ним можно сделать

month = int(input("Введите номер месяца:"))

def month_to_season(month):
    if (month in (12, 1, 2)):
        print("Зима")
    elif (month in (3, 4, 5)):
        print("Весна")
    elif (month in (6, 7, 8)):
        print("Лето")
    elif (month in (9, 10, 11)):
        print("Осень")
    else:
        print("в году только 12 месяцев")

month_to_season(month)