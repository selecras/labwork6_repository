print("Поиск медианы списка")

while True:
    try:
        lst = input("Введите элементы списка через пробел: ")
        lst = list(map(float, lst.split()))
        if not lst:
            continue
        break
    except ValueError:
        print("Некорректный ввод")

lst = sorted(lst)

if len(lst) % 2:
    result = lst[len(lst) // 2]
else:
    result = round((lst[len(lst) // 2] + lst[len(lst) // 2 - 1]) / 2, 2)

print(f"Медиана списка: {result}")
