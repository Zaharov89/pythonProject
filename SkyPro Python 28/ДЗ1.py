print("""Привет! Предлагаю проверить свои знания английского!
 Расскажи, как тебя зовут!""")

name = input()

print(f'Привет, {name}, начинаем тренировку!')

#Начинаем отсчет баллов и правильных ответов

number = 0
all_answer = 0

#Начинаем задания

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

percent = round(100 * all_answer / 3)  #Считаем проценты

#Изменяем окончания у слов в последнем сообщении для обучающегося
questions_ending = ""
if all_answer == 1:
    questions_ending = "вопрос"
elif 2 <= all_answer <= 4:
    questions_ending = "вопроса"
else:
    questions_ending = "вопросов"

scores_ending = ""
if number in (1, 21):
    scores_ending = "балл"
elif number in (2, 3, 4, 22, 23, 24):
    scores_ending = "балла"
else:
    scores_ending = "баллов"

percent_ending = ""
if percent in (1, 21, 31, 41, 51, 61, 71, 81, 91):
    percent_ending = "процент"
elif percent in (2, 3, 4, 22, 23, 24, 32, 33, 34, 42, 43, 44, 52, 53, 54, 62, 63, 64, 72, 73, 74, 82, 83, 84, 92, 93, 94):
    percent_ending = "процента"
else:
    percent_ending = "процентов"

print(f"""Вот и все, {name}! 
Вы ответили на {all_answer} {questions_ending} из 3 верно.
Вы заработали {number} {scores_ending}.
Это {percent} {percent_ending}.""")