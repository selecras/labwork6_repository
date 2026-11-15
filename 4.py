students = [
    ("Иван", 25, 4.5),
    ("Мария", 22, 4.8),
    ("Пётр", 30, 4.2),
    ("Тимур", 18, 4.6),
]

oldest = max(students, key=lambda x: x[1])
print(f"Самый старший: {oldest[0]}, {oldest[1]} лет")

best = max(students, key=lambda x: x[2])
print(f"Лучший студент: {best[0]}, балл {best[2]}")

avg_age = sum(s[1] for s in students) / len(students)
print(f"Средний возраст: {avg_age:.1f}")

sorted_students = sorted(students, key=lambda x: x[2])[::-1]
print("\nПо баллу:")
for name, age, gpa in sorted_students:
    print(f"{name}: {gpa}")
