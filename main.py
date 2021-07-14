from directories import *
from victory import victory_game
from bank import bank_game
from file_save import save_dir_content
import sys

print('Консольный файловый менеджер')
while True:
    print('1 - создать папку',
          '2 - удалить (файл/папку)',
          '3 - копировать (файл/папку)',
          '4 - просмотр содержимого рабочей директории',
          '5 - сохранить содержимое рабочей директории в файл',
          '6 - посмотреть только папки',
          '7 - посмотреть только файлы',
          '8 - просмотр информации об операционной системе',
          '9 - создатель программы',
          '10 - играть в викторину',
          '11 - мой банковский счет',
          '12 - смена рабочей директории (*необязательный пункт)',
          '13 - выход', sep='\n')
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
        save_dir_content()
        print('Содержимое рабочей директории сохранено')
        see_result = input('Посмотреть содержание? (1): ')
        if see_result == '1':
            with open('content_yaml.yaml', 'r') as f:
                dirs_and_files = f.read()
            print(dirs_and_files)
    elif inp == '6':
        dirs_list = show_dirs()
        print(dirs_list)
    elif inp == '7':
        files_list = show_files()
        print(files_list)
    elif inp == '8':
        print(sys.platform)
    elif inp == '9':
        print('Тимофей Егоров 11.07.2021')
    elif inp == '10':
        victory_game()
    elif inp == '11':
        bank_game()
    elif inp == '12':
        change_dir()
    elif inp == '13':
        break