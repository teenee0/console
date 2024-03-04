import os
import shutil

# Функция для создания папки
def create_folder(folder_name):
    try:
        os.mkdir(folder_name)
        print(f'Папка "{folder_name}" создана успешно')
    except FileExistsError:
        print(f'Папка "{folder_name}" уже существует')

# Функция для удаления папки
def delete_folder(folder_name):
    try:
        shutil.rmtree(folder_name)
        print(f'Папка "{folder_name}" удалена успешно')
    except FileNotFoundError:
        print(f'Папка "{folder_name}" не существует')

# Функция для перемещения между папками
def change_directory(folder_name):
    try:
        os.chdir(folder_name)
        print(f'Перешли в папку "{folder_name}"')
        return True
    except FileNotFoundError:
        print(f'Папка "{folder_name}" не существует')
        return False

# Функция для создания пустого файла
def create_file(file_name):
    with open(file_name, 'w') as file:
        pass
    print(f'Файл "{file_name}" создан успешно')

# Функция для записи текста в файл
def write_to_file(file_name, text):
    with open(file_name, 'w') as file:
        file.write(text)
    print(f'Текст записан в файл "{file_name}"')

# Функция для просмотра содержимого текстового файла
def read_file(file_name):
    try:
        with open(file_name, 'r') as file:
            print(file.read())
    except FileNotFoundError:
        print(f'Файл "{file_name}" не существует')

# Функция для удаления файла
def delete_file(file_name):
    try:
        os.remove(file_name)
        print(f'Файл "{file_name}" удален успешно')
    except FileNotFoundError:
        print(f'Файл "{file_name}" не существует')

# Функция для копирования файла
def copy_file(source, destination):
    try:
        shutil.copy(source, destination)
        print(f'Файл "{source}" скопирован в "{destination}"')
    except FileNotFoundError:
        print('Не удалось скопировать файл')

# Функция для перемещения файла
def move_file(source, destination):
    try:
        shutil.move(source, destination)
        print(f'Файл "{source}" перемещен в "{destination}"')
    except FileNotFoundError:
        print('Не удалось переместить файл')

# Функция для переименования файла
def rename_file(old_name, new_name):
    try:
        os.rename(old_name, new_name)
        print(f'Файл "{old_name}" переименован в "{new_name}"')
    except FileNotFoundError:
        print(f'Файл "{old_name}" не существует')

def show_directory(my_folder, directory):
    a = current_directory().split("\\").index(my_folder)
    # print(1, directory)
    # print(current_directory().split("\\"))
    b = current_directory().split("\\").index(directory)
    # print(a,b)
    mass = current_directory().split("\\")[a:b+1]

    for i in range(len(mass)):
        print(f'¬{mass[i]}')
        print("    " * (i+1), end="")
    print()


    # mass = current_directory().split("\\")[-2] папка где код

    # print(mass)



def show_files_in_current_directory():
    current_dir = os.getcwd()
    files = [f for f in os.listdir(current_dir) if os.path.isfile(os.path.join(current_dir, f))]
    for i in files:
        print(f'—{i}')

def show_folders_in_current_directory():
    current_dir = os.getcwd()
    folders = [f for f in os.listdir(current_dir) if os.path.isdir(os.path.join(current_dir, f))]
    for i in folders:
        print(f'¬{i}')



def previous_directory():
    current_dir = os.getcwd()
    parent_dir = os.path.dirname(current_dir)
    os.chdir(parent_dir)
    return parent_dir.split("\\")[-1]


# Главная функция для управления файловым менеджером
def current_directory():
    return os.getcwd()

def main():
    my_folder = current_directory().split("\\")[-1]
    print(f'Корневая папка кода - {my_folder}')
    # print("Создаем папку для теста...")
    if not os.path.exists("test"):
        print("Создаем папку для теста...")
        os.makedirs("test")
        print(f'Папка "{"test"}" создана успешно')
    else:
        print(f'Папка "{"test"}" уже существует')
    change_directory("test")
    # show_directory(my_folder, "test")
    # show_files_in_current_directory()
    now_dir = 'test'
    my_folder = current_directory().split("\\")[-1]
    while True:

        show_directory(my_folder, now_dir)
        print(os.getcwd())
        # print('\nДоступные действия:')
        # print('cr_fo. Создать папку')
        # print('de_fo. Удалить папку')
        # print('ch_dr. Перейти в папку')
        # print('cr_fi. Создать файл')
        # print('wr_to_fi. Записать текст в файл')
        # print('re_fi. Просмотреть содержимое файла')
        # print('de_fi. Удалить файл')
        # print('co_fi. Копировать файл')
        # print('mo_fi. Переместить файл')
        # print('re_fi. Переименовать файл')
        # print('q. Выйти')

        choice = input('Выберите действие: ')
        if choice == "1":
            show_directory(my_folder, now_dir)
            show_files_in_current_directory()
        elif choice == "2":
            show_folders_in_current_directory()
        elif choice == "3":
            if now_dir == my_folder:
                print("u cant")
                continue
            else:
                now_dir = previous_directory()

        elif choice == 'cr_fo':
            folder_name = input('Введите имя папки для создания: ')
            create_folder(folder_name)
        elif choice == 'de_fo':
            folder_name = input('Введите имя папки для удаления: ')
            delete_folder(folder_name)
        elif choice == 'ch_di':
            directory_name = input('Введите имя папки для перехода: ')
            if change_directory(directory_name):
                now_dir = directory_name

        elif choice == 'cr_fi':
            file_name = input('Введите имя файла для создания: ')
            create_file(file_name)
        elif choice == 'wr_to_fi':
            file_name = input('Введите имя файла для записи текста: ')
            text = input('Введите текст для записи в файл: ')
            write_to_file(file_name, text)
        elif choice == 're_fi':
            file_name = input('Введите имя файла для просмотра: ')
            read_file(file_name)
        elif choice == 'de_fi':
            file_name = input('Введите имя файла для удаления: ')
            delete_file(file_name)
        elif choice == 'co_fi':
            source = input('Введите имя исходного файла: ')
            destination = input('Введите имя папки для копирования: ')
            copy_file(source, destination)
        elif choice == 'mo_fi':
            source = input('Введите имя исходного файла: ')
            destination = input('Введите имя папки для перемещения: ')
            move_file(source, destination)
        elif choice == 're_fi':
            old_name = input('Введите текущее имя файла: ')
            new_name = input('Введите новое имя файла: ')
            rename_file(old_name, new_name)
        elif choice == 'q':
            break
        else:
            print('Некорректный ввод, попробуйте снова.')

        

        

        

        

if __name__ == '__main__':
    main()
