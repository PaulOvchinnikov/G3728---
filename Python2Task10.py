from random import randint

print("Привет! Это задание выполнено Павлом Овчинниковым при обучении основам языка Python")
print("""
Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом. 
Определите минимальное число монеток, которые нужно перевернуть, чтобы все монетки были повернуты 
вверх одной и той же стороной. Выведите минимальное количество монет, которые нужно перевернуть.
""")

coin_avers, coin_revers = 0, 0
coins = int(input('Введите количество монеток N: '))
N = coins
for _ in range(coins):
    coins = randint(0, 1)
    print(coins, end=' ')
    if coins == 0: 
       coin_avers += 1
    else: 
        coin_revers += 1
print()
print("Из ", N, "монеток - ", coin_avers, "выпали решкой и",  coin_revers, "орлом")
if coin_avers > coin_revers:
    print("Переворачиваем", coin_revers, "монет, выпавших орлом")
else:  print("Переворачиваем", coin_avers, "монет, выпавших решкой")

print()
print("Good luck! See you soon. The End.")
