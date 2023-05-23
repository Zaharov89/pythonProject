#month = ["Декабрь", "Январь", "Февраль", "Март", "Апрель", "Май", "Июнь", "Июль", "Август", "Сентябрь", "Октябрь", "Ноябрь"]

#winter = month[0: 3]
#spring = month[3: 6]
#summer = month[6: 9]
#autumn = month[9: 12]

# Список выше был лишним. Ничего не придумал, что с ним можно сделать

month = input("Введите номер месяца:")
month2 = int(month)
def month_to_season(month2):
    if (month2 in (12, 1, 2)):
        print("Зима")
    elif (month2 in (3, 5)):
        print("Весна")
    elif (month2 in (6, 8)):
        print("Лето")
    elif (month2 in (9, 11)):
        print("Осень")
    else:
        print("в году только 12 месяцев")

month_to_season(month2)