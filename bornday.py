question = int(input('Введите год рождения А. С. Пушкина:'))
if question == 1799:
        question_1 = float(input('Введите день рождения А. С. Пушкина:'))
        if question_1 == 25.05:
            print('Верно')
        else:
            print('Неверный день рождения')
else:
    print('Неверный год')