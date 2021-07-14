"""
МОДУЛЬ 3
Программа "Личный счет"
Описание работы программы:
Пользователь запускает программу у него на счету 0
Программа предлагает следующие варианты действий
1. пополнить счет
2. покупка
3. история покупок
4. выход

1. пополнение счета
при выборе этого пункта пользователю предлагается ввести сумму на сколько пополнить счет
после того как пользователь вводит сумму она добавляется к счету
снова попадаем в основное меню

2. покупка
при выборе этого пункта пользователю предлагается ввести сумму покупки
если она больше количества денег на счете, то сообщаем что денег не хватает и переходим в основное меню
если денег достаточно предлагаем пользователю ввести название покупки, например (еда)
снимаем деньги со счета
сохраняем покупку в историю
выходим в основное меню

3. история покупок
выводим историю покупок пользователя (название и сумму)
возвращаемся в основное меню

4. выход
выход из программы

При выполнении задания можно пользоваться любыми средствами

Для реализации основного меню можно использовать пример ниже или написать свой
"""
import os

ACCOUNT_SUM = 'acc_sum.txt'
PURCHASE_HYSTORY = 'perchase_hyst.txt'

def read_file(file_name):
    '''
    Фукция считывания файла
    :param file_name: название файла
    :return temp_: считанный с файла текст в виде строки
    '''
    with open(file_name, 'r') as f:
            temp_ = f.read()
    return temp_

def write_file(file_name, text_file):
    '''
    Функция записи в файл
    :param file_name:
    :return:
    '''
    with open(file_name, 'w') as f:
        f.write(f'{text_file}')

def bank_game():

    if os.path.exists(ACCOUNT_SUM):
        bank_account = int(read_file(ACCOUNT_SUM))
    else:
        bank_account = 0

    if os.path.exists(PURCHASE_HYSTORY):
        purchase_history = read_file(PURCHASE_HYSTORY)
    else:
        purchase_history = []

    temp_amount = 0
    temp_purchase = 0

    while True:
        print(f'У Вас на счету: {bank_account} рублей')
        print('1. пополнение счета')
        print('2. покупка')
        print('3. история покупок')
        print('4. выход')

        choice = input('Выберите пункт меню: ')

        if choice == '1':
            while True:
                temp_amount = input('Введите сумму для пополнения: ')
                try:
                    temp_amount = int(temp_amount)
                    break
                except ValueError:
                    print('Ошибка, введите целое число')
            bank_account += temp_amount

        elif choice == '2':
            while True:
                temp_amount = input('Введите сумму покупки: ')
                try:
                    temp_amount = int(temp_amount)
                    if temp_amount > bank_account:
                        print('Невозможно совершить покупку, сумма покупки больше суммы на счете')
                        break
                    bank_account -= temp_amount
                    temp_purchase = input('Введите название покупки: ')
                    purchase_history.append((temp_amount, temp_purchase))
                    break
                except ValueError:
                    print('Ошибка, введите целое число')
        elif choice == '3':
            print(purchase_history)
        elif choice == '4':
            write_file(ACCOUNT_SUM, bank_account)
            write_file(PURCHASE_HYSTORY, purchase_history)
            break

        else:
            print('Неверный пункт меню')

if __name__ == '__main__':
    bank_game()
