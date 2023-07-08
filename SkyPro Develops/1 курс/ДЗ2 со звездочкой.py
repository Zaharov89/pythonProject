user_input = input("Привет! Предлагаю проверить свои знания английского! Наберите \'ready\', чтобы начать! ")

# Создаем списки с вопросами и ответами

questions = ["My name ___ Vova", "I ___ a coder", "I live ___ Moscow"]
answers = ["is", "am", "in"]

all_correct_answer = 0
all_ball = 0

# Начинаем решать задачу

if user_input != 'ready':                                  # Создаем условие. Если не выпоняется, то все заканчивается
    print('Кажется, вы не хотите играть. Очень жаль')
else:                                                      # Начинаем задавать вопросы
    for i in range(len(questions)):
        print(questions[i])
        attempt = 3
        while attempt > 0:
#            print(questions[i])
            user_answer = input()
            if user_answer == answers[i]:
                print('Ответ верный!')
                all_correct_answer += 1
                all_ball += attempt
            else:
                attempt -= 1
                if user_answer != answers[i] and attempt != 0:
                    print(f'Неверно. Осталось попыток: {attempt}, попробуйте еще раз!')
                else:
                    print(f'Увы, но нет. Верный ответ: {answers[i]}')

    print(f'Вот и все! Вы ответили на {all_correct_answer} вопросов из {len(answers)} верно, вы набрали {all_ball} баллов')






