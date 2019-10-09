question = int(input('Введите год рождения А. С. Пушкина:'))
while question != 1799:
    question = int(input('Неверно, следующая попытка:'))
question_1 = float(input('Введите день рождения А. С. Пушкина:'))
while question != 25.05:
    question = float(input('Неверно, следующая попытка:'))
print('Верно')