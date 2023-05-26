from SkyPRO.Lesson_3.address import Address


class Mailing:

    def __init__(self, cost, track):
        self.cost = int(cost)
        self.track = str(track)

    def add_to(self):
        to_address = Address("351345", "Москва", "Ленина", "34", "11")            # Создаём ОБЪЕКТ КЛАССА
        to_address.say_to_address()                                               # Вызываем метод ИЗ ОБЪЕКТА

    def add_from(self):
        from_address = Address("325745", "Магадан", "Перова", "22", "55")         # Создаём ОБЪЕКТ КЛАССА
        from_address.say_from_address()                                           # Вызываем метод ИЗ ОБЪЕКТА


    # def say_from_address(self):
    #     print(self.from_address)
    #
    # def say_to_address(self):
    #     print(self.to_address)

    # def say_cost(self):
    #     print(self.cost)
    #
    # def say_track(self):
    #     print(self.track)
