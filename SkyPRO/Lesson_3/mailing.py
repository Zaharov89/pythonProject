from SkyPRO.Lesson_3.address import Address


class Mailing:

    def __init__(self, from_address, to_address, cost, track):
        self.from_address = from_address
        self.to_address = to_address
        self.cost = int(cost)
        self.track = str(track)

    # def add_from(self):
    #     from_address = Address("325745", "Магадан", "Перова", "22", "55")
    #     from_address.say_from_address()
    #
    # def add_to(self):
    #     to_address = Address("351345", "Москва", "Ленина", "34", "11")
    #     to_address.say_to_address()

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
