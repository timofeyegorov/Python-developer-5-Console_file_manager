import random
def victory_game():
    while True:
        data = {'Рубен Диаш': ['14.05.1997', 'Четырнадцатое мая 1997 года'],
                'Мохаммед Салах': ['15.06.1992', 'Пятнадцатое июня 1992 года'],
                'Кевин Де Брюйне': ['28.06.1991', 'Двадцать восьмое июня 1991 года'],
                'Неймар': ['05.02.1992', 'Пятое февраля 1992 года'],
                'Эрлинг Холланд': ['21.07.2000', 'Двадцать первое июля 2000 года'],
                'Килиан Мбаппе': ['20.12.1998', 'Двадцатое декабря 1998 года'],
                'Бруну Фернандеш': ['08.09.1994', 'Восьмое сентября 1994 года'],
                'Лионель Месси': ['24.06.1987', 'Двадцать четвертое июня 1987 года'],
                'Криштиану Роналду': ['05.02.1985', 'Пятое февраля 1985 года'],
                'Роберт Левандовски': ['21.08.1988', 'Двадцать первое августа 1988 года']
                }

        filtered_data = random.sample(list(data.keys()), 5)
        wrong, right = 0, 0
        for name in filtered_data:
            answer = input(f'Введите дату рождения {name} в формате dd.mm.yyyy: ')
            if answer != data[name][0]:
                print(f'Неверно, дата рождения {name} - {data[name][1]}')
                wrong += 1
            else:
                right += 1

        print('Правильных ответов: ', right)
        print('Ошибок: ', wrong)
        game = input('Сыграть еще? (введите нет, чтобы завершить игру): ')
        if game == 'нет':
            break
