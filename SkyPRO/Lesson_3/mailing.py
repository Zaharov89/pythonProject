from SkyPRO.Lesson_3 import address


class Mailing:

    def __init__(self, address.from_address(), address.to_address(), cost, track):
        self.from_address = address.from_address.say_from_address()
        self.to_address = address.to_address.say_to_address()
        self.cost = int(cost)
        self.track = str(track)

    def say_from_address(self):
        print(self.from_address)

    def say_to_address(self):
        print(self.to_address)

    def say_cost(self):
        print(self.cost)

    def say_track(self):
        print(self.track)

