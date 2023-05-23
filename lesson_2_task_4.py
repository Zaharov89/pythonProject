n = input("Введите число:")
n2 = int(n)
def fizz_buzz(n2):
    for n2 in range (1, n2):
        if ((n2 % 5 == 0) and (n2 % 3 == 0)):
            print("FizzBuzz")
        elif (n2 % 3 == 0):
            print("Fizz")
        elif (n2 % 5 == 0):
            print("Buzz")
        else:
            print(n2)

fizz_buzz(n2)
