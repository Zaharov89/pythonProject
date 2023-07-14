words_easy = {
    "family": "семья",
    "hand": "рука",
    "people": "люди",
    "evening": "вечер",
    "minute": "минута",
}

words_medium = {
    "believe": "верить",
    "feel": "чувствовать",
    "make": "делать",
    "open": "открывать",
    "think": "думать",
}

words_hard = {
    "rural": "деревенский",
    "fortune": "удача",
    "exercise": "упражнение",
    "suggest": "предлагать",
    "except": "кроме",
}

levels = {
   0: "Нулевой",
   1: "Так себе",
   2: "Можно лучше",
   3: "Норм",
   4: "Хорошо",
   5: "Отлично",
}

answers = {}

words_level = {'Легкий': words_easy,'Средний': words_medium,'Тяжелый': words_hard}    # Создаем словарь с разными уровнями

words = input('Введите уровень сложности словаря: ')                                  # Пользователь вводит желаемый уровень

point = words_level[words]                                                            # Копируем словарь с выбранным уровнем сложности от пользователя

for key, values in point.items():                                                     # Создаем цикл выбранного словаря с ключом и значением
    # Программа: divide, 9 букв, начинается на р...
    user_answer = input(f'{key}, {len(values)} букв, начинается на {values[0]}: ')
    if user_answer == values:
        answers[key] = True
        print(f'Верно, {key} — это {values}.')
    else:
        answers[key] = False
        print(f'Неверно. {key} — это {values}.')

# Когда слова закончились, выведите в зависимости от результата:
# Правильно отвечены слова:
# divide
# usual
# hidden
# mirror
#
# Неправильно отвечены слова:
# hero

print('Правильно отвечены слова: ')

numbers = 0

for word, word_values in answers.items():
    if word_values:
        numbers += 1
        print(word)

print('Неправильно отвечены слова: ')

for word, word_values in answers.items():
    if not word_values:
        print(word)

# Посчитайте количество правильно отгаданных слов, например, получив список ключей из answers. Используйте его в качестве ключа, чтобы получить ранг пользователя.

print(f'Ваш ранг: ', levels[numbers], sep='\n')