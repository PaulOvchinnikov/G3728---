print("Привет! Это задание выполнено Павлом Овчинниковым при обучении основам языка Python")
print()
print("Задача 2: Найдите сумму цифр трехзначного числа.")
print()

n = input("Введите 3х значное число: ")
print (n, len(n)," цифр(-ы)")
while len(n) != 3:
    number = int(n)
    if number < 100 or number > 999:
        n = input("Не, так не пойдет!!! 3 цифры, плиз! Введите правильно: ")

number = int(n)

a = int(n[0:1])
b = int(n[1:2])
c = int(n[2:3])

print ('Сумма цифр в числе ', {number}, ' равна ', {a + b + c})

print("Good luck! See you soon. The End.")