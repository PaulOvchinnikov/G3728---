
print("********************************************************************")
print("\t\tДобро пожаловать в телефонную книгу", flush=False)
print("********************************************************************")

file = open('phonebook.txt', 'r+', encoding='UTF-8')
lines_lst = file.readlines()
file.close()


def menu():
    print("\tМеню операций с данной телефонной книгой\n")
    print("1. Показать все контакты")
    print("2. Поиск контакта")
    print("3. Добавить новый контакт")
    print("4. Удалить контакт")
    print("5. Редактировать контакт")
    print("6. Удалить все контакты")
    print("7. Выйти из программы")
    choice = 0
    while (choice < 1) or (choice > 7):
        choice = int(input("\nВыберите пункт меню: "))
        if (choice < 1) or (choice > 7):
            print("Не, так не пойдет! Введите пункт меню правильно! от 1 до 7: ")
    return choice


def find_cont(lines_lst):  # Функция поиска
    search_cont = input('Введите информацию для поиска: ')
    for cont in lines_lst:
        if search_cont.lower() in cont.lower():
            print(cont)


def add_cont(lines_lst):
    second_name = input('Введите фамилию: ')
    first_name = input('Введите имя: ')
    tel = input('Пожалуйста введите номер телефона: ')
    comment = input('Введите комментарий: ')

    new_cont = str(len(lines_lst))+"\t"+second_name + \
        "\t"+first_name+"\t"+tel+"\t"+comment+"\n"
    lines_lst.append(new_cont)
    print("Контакт добавлен:", new_cont)


def del_cont(del_name):
    temp = 0
    i = 0
    for cont in lines_lst:
        if del_name.lower() in cont.lower():
            temp += 1
            print("Удален контакт: ", lines_lst.pop(i))
            return lines_lst
        i += 1
    if temp == 0:
        print("Извините, такой контакт не найден!")
        return lines_lst


def change_cont():
    name = input("Пожалуйста, введите контакт для редактирования: ")
    for cont in lines_lst:
        if name.lower() in cont.lower():
            print(cont)
            add_cont(lines_lst)
            del_cont(name)
    else:
        print("Контакт не найден!")


def delete_all(lines_lst):
    print("Мне жалко всё удалять! Простая команда lines_lst.clear() и нет никого :)")
    return lines_lst


# Выполнение
while True:
    x = menu()
    if x == 1:
        print(''.join(lines_lst))
    elif x == 2:
        find_cont(lines_lst)
    elif x == 3:
        add_cont(lines_lst)
    elif x == 4:
        del_name = str(input("Пожалуйста, введите контакт для удаления: "))
        del_cont(del_name)
        # print('\n'.join(lines_lst))
    elif x == 5:
        change_cont()
    elif x == 6:
        delete_all(lines_lst)
    elif x == 7:
        y = input("\nСохранить внесенные изменения? Y/N ")
        if y == 'y' or 'Y':
            file = open('phonebook.txt', 'w+', encoding='UTF-8')
            file.writelines(lines_lst)
            file.close()
        print("Спасибо за пользование телефонной книгой. До новых встреч!")
        break
