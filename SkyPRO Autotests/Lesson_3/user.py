class User:

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def say_f_Name(self):
        print(self.first_name)

    def say_l_Name(self):
        print(self.last_name)

    def say_f_l_Name(self):
        print(self.first_name, self.last_name)