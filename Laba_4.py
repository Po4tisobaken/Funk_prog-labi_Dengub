from functools import partial  # Фиксирует часть аргументов функции.


# Уровень 1. Каррирование: ключ → значение → список.
# lambda создаёт короткую функцию без def.
# Чистая: зависит от аргументов, исходные список и словари не меняет.
filter_by = lambda key: lambda value: lambda items: [
    item for item in items if key in item and item[key] == value  # Без ключа — пропуск.
]


# Уровень 2. partial фиксирует ключ category.
# Обёртка передаёт три аргумента в цепочку filter_by.
# Чистая: вызывает чистую filter_by с заранее заданным ключом.
filter_by_category = partial(
    lambda key, value, items: filter_by(key)(value)(items),
    "category",
)


# Уровень 3. Сначала задаём порог, потом передаём число.
# Чистая: только сравнивает числа, не меняя данные и внешнее состояние.
greater_than = lambda threshold: lambda x: x > threshold


# Проверка работы. Вывод находится за пределами чистых функций.
items = [
    {"name": "apple", "category": "fruit"},
    {"name": "carrot", "category": "vegetable"},
    {"name": "banana", "category": "fruit"},
]

print("Фрукты через каррирование:")
print(filter_by("category")("fruit")(items))

filter_fruits = partial(filter_by_category, "fruit")  # Фиксируем ещё и значение.
print("\nФрукты через partial:")
print(filter_fruits(items))

numbers = [1, 6, 8, 2, 9]
over_five = greater_than(5)  # Готовая функция проверки x > 5.
print("\nЧисла больше пяти:")
print(list(filter(over_five, numbers)))  # filter отбирает, list собирает список.


# Уровень 4. Рефлексия:
# Каррирование позволяет задать часть аргументов заранее и переиспользовать
# полученную функцию. Например, over_five подходит для разных списков чисел.
# Без каррирования тоже можно: передавать все аргументы при каждом вызове
# или сразу написать условие отбора в lambda.
# partial также фиксирует аргументы, но может работать с обычными функциями,
# принимающими несколько аргументов сразу.
# Функции создают новые списки, не меняют исходные данные и не делают вывод.
# При одинаковых аргументах результат одинаковый; пустой список даёт [].
