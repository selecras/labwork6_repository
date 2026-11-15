from random import choice, randint


def partition(lst: list) -> list:
    elem = choice(lst)
    result = [[], [], []]
    # делим список на три части -- меньше опорного элемента, равные ему, и больше него
    for i in lst:
        if i < elem:
            result[0].append(i)
        elif i == elem:
            result[1].append(i)
        else:
            result[2].append(i)
    return result


def quicksort(lst: list):
    # если длина списка <= 1, то он очевидно отсортирован
    if len(lst) <= 1:
        return lst

    # делим на три части
    a = partition(lst)
    left = a[0]
    elems = a[1]
    right = a[2]

    # рекурсивно сортируем левую и правую части
    left = quicksort(left)
    right = quicksort(right)

    return left + elems + right


if __name__ == "__main__":
    while True:
        try:
            N = int(input("Введите кол-во элементов: "))
            if not (1 <= N <= 50):
                raise ValueError
            break
        except ValueError:
            print("Некорректный ввод")

    a = [randint(1, 100) for _ in range(N)]
    sorted_a = quicksort(a)
    print(a)
    print(sorted_a)
