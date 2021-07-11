from directories import *
from victory import victory_game
from bank import bank_game

print('Консольный файловый менеджер')
while True:
    print('1 - создать папку',
          '2 - удалить (файл/папку)',
          '3 - копировать (файл/папку)',
          '4 - просмотр содержимого рабочей директории',
          '5 - посмотреть только папки',
          '6 - посмотреть только файлы',
          '7 - просмотр информации об операционной системе',
          '8 - создатель программы',
          '9 - играть в викторину',
          '10 - мой банковский счет',
          '11 - смена рабочей директории (*необязательный пункт)',
          '12 - выход', sep='\n')
    inp = input('Выберите пункт меню: ')

    if inp == '1':
        create_dir()
    elif inp == '2':
        delete_dir_file()
    elif inp == '3':
        copy_dir_file()
    elif inp == '4':
        print(os.listdir())
    elif inp == '5':
        show_dirs()
    elif inp == '6':
        show_files()
    elif inp == '7':
        pass
    elif inp == '8':
        print('Тимофей Егоров 11.07.2021')
    elif inp == '9':
        victory_game()
    elif inp == '10':
        bank_game()
    elif inp == '11':
        change_dir()
    elif inp == '12':
        break
