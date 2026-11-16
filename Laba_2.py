import re  # Поиск слов по шаблону.
from typing import Optional  # Тип результата допускает None.

# Уровень 1. Разбиваем текст на слова.
# Чистая: результат зависит только от text, создаётся новый список.
def split_words(text: str) -> list[str]:
    words = re.findall(r"[^\W_]+", text)  # Буквы и цифры без пунктуации и _.
    # map применяет lambda к каждому слову, lower понижает регистр.
    return list(map(lambda word: word.lower(), words))


# Уровень 2. Считаем вхождения каждого слова.
# Чистая: одинаковые слова дают одинаковые частоты, words не меняется.
def count_word_frequencies(words: list[str]) -> dict[str, int]:
    return {
        word: sum(map(lambda item: item == word, words))  # True даёт 1, False — 0.
        for word in dict.fromkeys(words)  # fromkeys оставляет уникальные слова.
    }


# Уровень 3. Находим самое частое слово рекурсией.
# Чистая: только читает freq, для пустого словаря возвращает None.
def top_word(freq: dict[str, int]) -> Optional[str]:
    if not freq:
        return None

    items = list(freq.items())  # Пары (слово, частота).

    # Делим диапазон пополам, чтобы глубина рекурсии росла медленно.
    # Чистая: читает локальный items без изменения данных.
    def find_best(start: int, end: int) -> tuple[str, int]:
        if end - start == 1:  # Одно слово — конец рекурсии.
            return items[start]

        middle = (start + end) // 2
        left = find_best(start, middle)  # Лучшее слово в левой половине.
        right = find_best(middle, end)
        return left if left[1] >= right[1] else right

    return find_best(0, len(items))[0]  # Из найденной пары берём только слово.


# ============ Проверка работы функций ============
# Вывод на экран — побочный эффект только демонстрационной части.

text = """Чистые функции делают код понятнее.
Функции без побочных эффектов проще проверять"""

words = split_words(text)
freq = count_word_frequencies(words)

print("Слова:")
print(words)

print("\nЧастотность слов:")
print(freq)

print("\nСамое частое слово:")
print(top_word(freq))

print("\nПроверка на пустую строку:")
print(split_words(""))

print("\nПроверка пустого словаря:")
print(top_word({}))


# ============ Уровень 4. Рефлексия ============

# 1. Побочных эффектов нет:
#    - функции ничего не выводят на экран и не записывают в файлы;
#    - не используют внешнее состояние;
#    - не изменяют переданные список и словарь.
#
# 2. Функции детерминированы:
#    при одинаковых аргументах они возвращают одинаковый результат.
#
# 3. Пустая строка:
#    split_words("") -> []
#
# 4. Пустой словарь:
#    top_word({}) -> None
#    Вся цепочка для пустой строки: [] -> {} -> None.
#
# 5. Функции определены для входов указанных типов, включая пустые коллекции.
#    При равных частотах top_word выбирает первое слово в порядке словаря.
