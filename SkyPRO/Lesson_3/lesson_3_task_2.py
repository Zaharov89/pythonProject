from smartphone import Smartphone

catalog = []

catalog.append(Smartphone("Xiaomi", "MI5", "+79286667743"))
catalog.append(Smartphone("Samsung", "Galaxy", "+79286664455"))
catalog.append(Smartphone("Sony", "N6", "+79286663263"))
catalog.append(Smartphone("Nokia", "1100", "+79234767743"))
catalog.append(Smartphone("Apple", "13", "+792897127743"))

for smarthone in catalog:
    smarthone.say_smartphone()
