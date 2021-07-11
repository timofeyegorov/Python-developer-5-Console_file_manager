import os
import shutil

def create_dir():
    dir_name = input('Введите название новой папки: ')
    os.mkdir(dir_name)
    print(f'Папка {dir_name} создана')
    print(os.listdir(os.getcwd()))

def delete_dir_file():
    while True:
        print('1 - удалить папку', '2 - удалить файл', '3 - выход', sep='\n')

        choice = input('Выберите пукт меню: ')
        if choice == '1':
            print('Папки в текущей директории: ')
            show_dirs()
            dir_name = input('Введите название папки которую нужно удалить: ')
            try:
                shutil.rmtree(dir_name)
                print(f'Папка {dir_name} удалена')
                print(os.listdir(os.getcwd()))
            except FileNotFoundError:
                print(f'Папка {dir_name} не найдена')


        elif choice == '2':
            print('Папки в текущей директории: ')
            show_files()
            file_name = input('Введите название файла который нужно удалить: ')
            try:
                os.remove(file_name)
                print(f'Файл {file_name} удален')
                print(os.listdir(os.getcwd()))
            except FileNotFoundError:
                print(f'Файл {file_name} не найден')

        elif choice == '3':
            break

        else:
            print('Пункт меню не распознан, попробуйте еще раз: ')


def copy_dir_file():
    while True:
        print('1 - копировать папку', '2 - копировать файл', '3 - выход', sep='\n')

        choice = input('Выберите пукт меню: ')
        if choice == '1':
            print('Папки в текущей директории: ')
            show_dirs()
            dir_name = input('Введите название папки которую нужно копировать: ')
            dir_name_new = input('Введите название новой папки: ')
            try:
                shutil.copytree(dir_name, dir_name_new)
                print(f'Папка {dir_name} скопирована')
                print(os.listdir(os.getcwd()))
            except FileNotFoundError:
                print(f'Папка {dir_name} не найдена')


        elif choice == '2':
            print('Файлы в текущей директории: ')
            show_files()
            file_name = input('Введите название файла который нужно скопировать: ')
            file_name_new = input('Введите название нового файла: ')
            try:
                shutil.copyfile(file_name, file_name_new)
                print(f'Файл {file_name} скопирован')
                print(os.listdir(getcwd()))
            except FileNotFoundError:
                print(f'Файл {file_name} не найден')

        elif choice == '3':
            break

        else:
            print('Пункт меню не распознан, попробуйте еще раз: ')

def show_dirs():
    for el in os.listdir(os.getcwd()):
        if os.path.isdir(os.path.join('.', el)) == True:
            print(el)

def show_files():
    for el in os.listdir(os.getcwd()):
        if os.path.isdir(os.path.join('.', el)) == False:
            print(el)

def change_dir():
    while True:
        ch_dir = input('Укажите путь до новой директории: ')
        try:
            os.chdir(ch_dir)
            print('Текущая директроия изменена: ')
            print(os.getcwd())
            break
        except FileNotFoundError:
            print('Несуществующий путь, проверьте корректность')
