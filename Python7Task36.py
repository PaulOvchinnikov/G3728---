print('''
Задача 36: Напишите функцию print_operation_table(operation, num_rows=6, num_columns=6), 
которая принимает в качестве аргумента функцию, вычисляющую элемент по номеру строки и столбца. 
Аргументы num_rows и num_columns указывают число строк и столбцов таблицы, 
которые должны быть распечатаны. Нумерация строк и столбцов идет с единицы (подумайте, почему не с нуля).
''')


def print_operation_table(operation, num_rows, num_columns):
    for i in range(0, num_rows + 1):
        table = []
        for j in range(0, num_columns + 1):
            if i==0:
                table.append(str(j))
            elif j==0:
                table.append(str(i))
            else:
                table.append(str(operation(i, j)))
        print("\t".join(table))

x = int(input("Введете число строк: "))
y = int(input("Введете число столбцов: "))

print(f"Таблица умножения", x, "на", y)
print_operation_table(lambda x, y: x * y, x, y)

print(f"Таблица сложения", x, "на", y)
print_operation_table(lambda x, y: x + y, x, y)

print(f"Таблица вычитания", x, "на", y)
print_operation_table(lambda x, y: x - y, x, y)

print(f"Таблица возведение в степень", x, "на", y)
print_operation_table(lambda x, y: x ** y, x, y)