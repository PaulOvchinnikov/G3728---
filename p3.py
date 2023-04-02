

print('''
Напишите функцию, которая принимает одно число и проверяет, является ли оно простым
''')


def simple(number):
    for i in range(2, 9):
        if number %i == 0:
            print ("число ", number, "делится на ", i)
            return
        else:
            return print ("число ", number, "простоe")

number = int(input("Введите число: "))
simple(number)
