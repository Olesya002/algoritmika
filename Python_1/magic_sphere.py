from random import randint
# список в отдельный модуль
answers = ["Бесспорно", "Мне кажется - да", "Пока неясно, попробуй снова", "Даже не думай",
           "Предрешено", "Вероятнее всего", "Спроси позже", "Мой ответ - нет",
           "Никаких сомнений", "Хорошие перспективы", "Лучше не рассказывать", "По моим данным - нет",
           "Можешь быть уверен в этом", "Да", "Сконцентрируйся и спроси опять", "Весьма сомнительно"]

print('Привет Мир, я магический шар, и я знаю ответ на любой твой вопрос.')
name = input('Введите Ваше имя: ')
print('Привет,', name)

while True:
    question = input('Задавайте вопрос: ')
    print(answers[randint(0, len(answers))])
    ans = input('Хотетие задать еще вопрос?')
    if ans == 'да' or ans == 'yes':
        continue
    else:
        print(name, ', возращайся еще если возникнут вопросы!')
        break
