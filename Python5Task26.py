print('''
Задача 26:  Напишите программу, которая на вход принимает два числа A и B, и возводит число А в целую степень B с помощью рекурсии.
''')

def exponentiation(number, exp):
    if (exp == 0):
        return 1
    elif (exp == 1):
        return number
    elif (exp != 1):
        return (number * exponentiation(number, exp-1))

# Main performance
number = int(input("Введите число: "))
exp = int(input("Введите его степень: "))
print()
print("Результат возведения числа", number, "в степень", exp, "равен:", exponentiation(number, exp))