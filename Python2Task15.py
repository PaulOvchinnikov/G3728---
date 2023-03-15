from random import randint
count = int(input('Введите количество арбузов: '))

min_weight = 30000
max_weight = 1000
for _ in range(count):
    current_weight = randint(1000, 30000)
    print(current_weight, end=' ')
    if min_weight > current_weight:
        min_weight = current_weight
    if max_weight < current_weight:
        max_weight = current_weight

print(f'\nСебе {max_weight/1000}кг, а тёще {min_weight/1000}кг')