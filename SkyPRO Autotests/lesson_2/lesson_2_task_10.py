x = int(input("Введите сумму вклада в рублях:"))
y = int(input("Введите на сколько лет берете вклад:"))

def bank (x, y):
    for each_year in range(y):
        x = (x * 1.1)
    return x

print(bank(x, y))
