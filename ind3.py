from random import randint
from ind2 import quicksort


def binary_search(lst: list, to_find: int | float) -> int | None:
    low = 0
    high = len(lst) - 1
    while low <= high:
        mid = (low + high) // 2
        elem = lst[mid]
        if elem == to_find:
            return mid
        elif to_find > elem:
            low = mid + 1
        else:
            high = mid - 1
    return None


if __name__ == "__main__":
    print("""Бинарный поиск 
Режимы работы: 
1. Ввести массив вручную 
2. Случайный массив из N элементов 
    """)
    ans = input("Ваш выбор: ")

    while ans not in ("1", "2"):
        print("Некорректный ввод")
        ans = input("Ваш выбор: ")

    if ans == "1":
        while True:
            try:
                lst = list(map(float, input("Введите числа через пробел: ").split()))
                break
            except ValueError:
                print("Некорректный ввод")
    elif ans == "2":
        while True:
            try:
                n = int(input("Введите количество элементов: "))
                if not (1 <= n <= 1000):
                    raise ValueError

                a = int(input("Введите нижнюю границу: "))
                b = int(input("Введите верхнюю границу: "))
                if a >= b:
                    raise ValueError

                break
            except ValueError:
                print("Некорректный ввод")
        lst = [randint(a, b) for _ in range(n)]
    lst = quicksort(lst)
    print(f"Готовый список:", end=" ")
    print(*lst, sep=", ")

    while True:
        try:
            to_find = float(input("Элемент для поиска: "))
            break
        except ValueError:
            print("Некорректный ввод")
    print()

    result = binary_search(lst, to_find)
    if result is not None:
        print(f"Элемент {to_find} найден под индексом {result}")
    else:
        print(f"Элемент {to_find} не был найден")
