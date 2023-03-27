print('''
Задача 28: Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых неотрицательных чисел. Из всех арифметических операций допускаются только +1 и -1. Также нельзя использовать циклы.
''')

def sum(number_1, number_2):
    if number_1 == 0:
        return number_2
    elif number_2 == 0:
        return number_1
    return sum(number_1-1, number_2+1)

# Main performance

number_1 = int(input("Введите первое слагаемое: "))
number_2 = int(input("Введите второе слагаемое: "))
print()
print("Результат суммы двух чисел", number_1, "и", number_2, "равен:", sum(number_1, number_2))
