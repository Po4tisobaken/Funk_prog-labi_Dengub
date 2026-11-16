from functools import reduce  # Сворачивает элементы в одно значение.
from typing import Optional  # Тип результата допускает None.


# Допустимые входы — записи студентов указанного в задании вида.
# Уровень 1. map применяет lambda к каждому студенту.
# Чистая: создаёт строки из аргумента, не меняя записи студентов.
def describe_students(students: list[dict]) -> list[str]:
    return list(map(
        lambda student: f"Имя: {student['name']}, Оценка: {student['grade']}",
        students,
    ))


# Уровень 2. filter оставляет студентов, для которых условие True.
# Чистая: возвращает новый список, исходные данные остаются прежними.
def select_good_students(students: list[dict]) -> list[dict]:
    return list(filter(lambda student: student["grade"] > 4.0, students))


# Уровень 3. Складываем возраст через reduce и делим на число студентов.
# Чистая: считает только по аргументу; пустой список даёт None без ошибки.
def average_age(students: list[dict]) -> Optional[float]:
    if not students:  # У пустого списка средний возраст не определён.
        return None

    # total накапливает возраст, 0 — начальная сумма.
    total_age = reduce(lambda total, student: total + student["age"], students, 0)
    return total_age / len(students)  # Сумма возрастов / число студентов.


# Проверка работы. Вывод находится за пределами чистых функций.
students = [
    {"name": "Анна", "age": 20, "grade": 4.5},
    {"name": "Борис", "age": 22, "grade": 3.8},
    {"name": "Виктор", "age": 19, "grade": 4.2},
    {"name": "Галина", "age": 21, "grade": 4.9},
    {"name": "Дмитрий", "age": 23, "grade": 3.5},
]

print("Описания студентов:")
print(describe_students(students))

selected_students = select_good_students(students)
print("\nСтуденты с оценкой выше 4.0:")
print(selected_students)

print("\nСредний возраст отобранных студентов:")
print(average_age(selected_students))

print("\nСредний возраст для пустого списка:")
print(average_age([]))


# Уровень 4. Рефлексия:
# map и filter сразу показывают, что мы преобразуем и отбираем данные.
# В императивном варианте пришлось бы писать циклы, добавлять элементы
# в списки и отдельно обновлять сумму возрастов.
# Короткие lambda читаются легко, но сложное выражение внутри reduce
# может быть менее понятным, чем обычный цикл.
# В цикле легко ошибиться со счётчиком, суммой или изменить исходный список.
# В обоих подходах нужно проверять пустой список, иначе возможно деление на ноль.
# Здесь средний возраст пустого списка — None, а не ошибка.
# Функции работают со словарями указанного в задании вида, не меняют аргументы,
# не зависят от внешних данных и при одинаковом входе дают одинаковый результат.
