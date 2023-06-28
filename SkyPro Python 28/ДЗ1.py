print("""Привет! Предлагаю проверить свои знания английского!
 Расскажи, как тебя зовут!""")

name = input()

print(f'Привет, {name}, начинаем тренировку!')

number = 0
all_answer = 0

print("My name ___ Vova")

answer_1 = input()

if answer_1 == "is":
    number += +10
    all_answer += 1
    print("""Ответ верный!
Вы получаете 10 баллов!""")
else:
    print("""Неправильно.
Правильный ответ: is""")


print("I ___ a coder")

answer_2 = input()

if answer_2 == "am":
    number += +10
    all_answer += 1
    print("""Ответ верный!
Вы получаете 10 баллов!""")
else:
    print("""Неправильно.
Правильный ответ: am""")

print("I live ___ Moscow")

answer_3 = input()

if answer_3 == "in":
    number += +10
    all_answer += 1
    print("""Ответ верный!
Вы получаете 10 баллов!""")
else:
    print("""Неправильно.
Правильный ответ: in""")

percent = 100 * all_answer / 3

print(f"""Вот и все, {name}! 
Вы ответили на {all_answer} вопросов из 3 верно.
Вы заработали {number} баллов.
Это {percent} процентов.""")