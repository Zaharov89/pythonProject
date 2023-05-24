from smartphone import Smartphone

#catalog = [
#    "Xiaomi", "MI5", "+79286667743",
#    "Samsung", "Galaxy", "+79286664455",
#    "Sony", "N6", "+79286663263",
#    "Nokia", "1100", "+79234767743",
#    "Apple", "13", "+792897127743",
#]

#print(catalog)


smartphone_1 = Smartphone("Xiaomi", "MI5", "+79286667743")
smartphone_2 = Smartphone("Samsung", "Galaxy", "+79286664455")
smartphone_3 = Smartphone("Sony", "N6", "+79286663263")
smartphone_4 = Smartphone("Nokia", "1100", "+79234767743")
smartphone_5 = Smartphone("Apple", "13", "+792897127743")

smartphone_1.say_smartphone()
smartphone_2.say_smartphone()
smartphone_3.say_smartphone()
smartphone_4.say_smartphone()
smartphone_5.say_smartphone()

catalog = [smartphone_1.say_smartphone(), smartphone_2.say_smartphone(), smartphone_3.say_smartphone(), smartphone_4.say_smartphone(), smartphone_5.say_smartphone()]

print(catalog)