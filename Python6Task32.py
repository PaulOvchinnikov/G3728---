import random
print(''' Задача 32: Определить индексы элементов массива (списка), значения которых принадлежат 
заданному диапазону (т.е. не меньше заданного минимума и не больше заданного максимума)
''')

def random_array(arr_min, arr_max, n):
    # min_arr, max_arr - диапазон эл.массива, n - кол-во
    return list(r(arr_min, arr_max) for r in [random.randint] * n)


def index_array(array, n_min, n_max):
    array_1 = []
    for i in range(n):
        if array[i] >= n_min and array[i] <= n_max:
            array_1.append(i)
    return (array_1)

# print()
n = int(input("Введите кол-во элементов массива: "))
arr_min = int(input("Введите значение минимума диапазона поиска от 0 до 10: "))
arr_max = int(input("Введите значение максимума диапазона поиска от 0 до 10: "))

temp_array=list(random_array(0, 10, n))
# print(index_array(random_array(0, 10, n), arr_min, arr_max), end=" ")
print(temp_array)
print(f"Индексы элементов списка, значения которых в диапазоне от", arr_min, "до", arr_max, ":", end=" ")
print(index_array(temp_array, arr_min, arr_max))