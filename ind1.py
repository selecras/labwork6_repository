from random import randint


def merge_sort(lst: list) -> list:
    # если список содержит один элемент, он уже отсортирован
    if len(lst) <= 1:
        return lst

    # делим список на левую и правую части
    ind = len(lst) // 2
    left = lst[:ind]
    right = lst[ind:]

    # рекурсивно сортируем половины
    left = merge_sort(left)
    right = merge_sort(right)

    return merge(left, right)


def merge(left: list, right: list) -> list:
    result = []
    # цикл пока оба левый и правый списки непустые
    while left and right:
        # сравниваем первые элементы
        if left[0] > right[0]:
            result.append(right.pop(0))
        else:
            result.append(left.pop(0))
    # вставляем в result то, что осталось
    result.extend(left or right)
    return result


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
    sorted_a = merge_sort(a)
    print(a)
    print(sorted_a)
