# print("Привет! Это задание выполнено Павлом Овчинниковым при обучении основам языка Python")
print("""
По данному целому неотрицательному n вычислите значение n!. 
N! = 1 * 2 * 3 * … * N (произведение всех чисел от 1 до N) 0! = 1 
Решить задачу используя цикл while
""")
n = -1
while (n < 0) or (n > 100):
    n = int(input("Введите число N: "))

factorial_n = 1
if n == 0:
    factorial_n = 1
else:
    i = 1
    while i < n:
        factorial_n = factorial_n * i
        i=i+1
    
print("Факториал числа", n, "равен ", factorial_n)

# print("Good luck! See you soon. The End.")
