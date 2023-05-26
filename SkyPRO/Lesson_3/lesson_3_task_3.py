from SkyPRO.Lesson_3.mailing import Mailing
from SkyPRO.Lesson_3.address import Address


#my_mailing = (
#"Отправление", mailing.say_track(), "из", mailing.say_from_address2(), "в", mailing.say_to_address2(), "Стоимость",
#mailing.say_cost(), "рублей.")


my_mailing = Mailing("325745", "Магадан", "Перова", "22", "55", "351345", "Москва", "Ленина", "34", "11", 123, "123")

print(my_mailing)
