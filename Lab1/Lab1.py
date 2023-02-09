# Из списка удалить четные элементы,
# имеющие значение больше среднего
# арифметического всех элементов списка.

import random

from numpy import number


# валидация ввода - ввод должен быть не пустой и каждый элемент должен быть типа int
def valid_input(input):
    return all(x.isdigit() for x in input) and len(input) > 0


# считаем среднее арифметическое
def middle(list):
    middle_result = 0
    for i in list:
        middle_result += i
    return middle_result / len(list)


# фильтрую список
def filterList(list):
    mid = middle(list)
    # создаю список, в который буду добавлять только нечётные, не больше среднего арифметического
    final_list = []
    for i in range(len(list)):
        if list[i] < mid or list[i] % 2 != 0:
            final_list.append(list[i])
    print(final_list)

# проверка выбранного метода ввода
def input_method(method):
    if method == "1":
        print("Введите список чисел через пробел")
        list_input = input().split()

        if valid_input(list_input):
            return list(map(int, list_input))
        else:
            print("Ввод неверный, введите список чисел")
            return 0

    if method == "2":
        length: int = int(input("Введите длину списка\n"))
        return [random.randint(0, 10) for _ in range(0, length)]


def requestUser():
    print("Выберите способ ввода: 1 - вручную, 2 - автогенерация")

    user_input_type = input()

    if not valid_input(user_input_type):
        print("Неверный ввод, введите 1 или 2")
        return
    else:
        numbers = input_method(user_input_type)
        if numbers == 0:
            return
        if user_input_type == "2":
            print("Автоматически сгенерированный список: "  f"{numbers}")

    print("Выберите метод обработки: 1 - нестандартные функции, 2 - стандартные")

    method: str = input()

    if not valid_input(method):
        print("Неверный ввод, введите 1 или 2")
        return
    if method == "1":
        filterList(numbers)
    if method == "2":
        print(list(filter(lambda it: it < middle(numbers) or it % 2 != 0, numbers)))


requestUser()
