from SkyPRO.Lesson_3.mailing import Mailing, Address


#my_mailing = (
#"Отправление", mailing.say_track(), "из", mailing.say_from_address2(), "в", mailing.say_to_address2(), "Стоимость",
#mailing.say_cost(), "рублей.")

to_address = Address("351345", "Москва", "Ленина", "34", "11")
from_address = Address("325745", "Магадан", "Перова", "22", "55")



my_mailing = Mailing(from_address, to_address, 123, "123")

print("Отпарвление {} из {}, {}, {}, {}-{} в {}, {}, {}, {}-{}. Стоимость {} рублей."
      .format(my_mailing.track, to_address.index, to_address.city, to_address.street, to_address.house, to_address.appartment,
              from_address.index, from_address.city, from_address.street, from_address.house, to_address.appartment, my_mailing.cost))


