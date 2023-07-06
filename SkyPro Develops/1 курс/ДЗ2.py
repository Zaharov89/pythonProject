print("Привет! Предлагаю проверить свои знания английского! Наберите \'ready\', чтобы начать!")

user_input = input()

# Создаем списки с вопросами и ответами

questions = ["My name ___ Vova", "I ___ a coder", "I live ___ Moscow"]
answers = ["is", "am", "in"]

all_answer = 0

# Начинаем решать задачу

if user_input != 'ready':                                  # Создаем условие. Если не выпоняется, то все заканчивается
    print('Кажется, вы не хотите играть. Очень жаль')
else:                                                      # Начинаем задавать вопросы
    for i in range(len(questions)):
        print(questions[i])
        user_answer = input()
        if user_answer == answers[i]:
            print('Ответ верный!')
            all_answer += 1
        else:
            print(f'Неправильно. Правильный ответ: {answers[i]}')
print(f'Вот и все! Вы ответили на {all_answer} вопросов из {len(answers)} верно, это {round(100 * all_answer / len(answers))} процентов.')




