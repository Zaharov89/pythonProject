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
percent_round = round(percent)

stile_answer = all_answer

if stile_answer == 1:
    print("вопрос")
elif 2 <= stile_answer <= 4:
    print("вопроса")
else:
    print("вопросов")

stile_number = number

if stile_number == (1, 21):
    print("балл")
elif stile_number == (2, 3, 4, 22, 23, 24):
    print("балла")
else:
    print("баллов")

stile_percent = percent_round

if stile_percent == (1, 21, 31, 41, 51, 61, 71, 81, 91):
    print("процент")
elif stile_answer == (2, 3, 4, 22, 23, 24, 32, 33, 34, 42, 43, 44, 52, 53, 54, 62, 63, 64, 72, 73, 74, 82, 83, 84, 92, 93, 94):
    print("процента")
else:
    print("процентов")

print(f"""Вот и все, {name}! 
Вы ответили на {all_answer} {stile_answer} из 3 верно.
Вы заработали {number} {stile_number}.
Это {percent_round} {stile_percent}.""")