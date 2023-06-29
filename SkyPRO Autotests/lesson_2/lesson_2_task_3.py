import math

side_of_the_square = float(input("Введите значение стороны квадрата:"))
def square(side_of_the_square):
    print(math.ceil(side_of_the_square * side_of_the_square))

square(side_of_the_square)

