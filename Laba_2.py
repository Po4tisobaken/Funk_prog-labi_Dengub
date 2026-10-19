import re
from typing import Optional


# Принимает - str
# Возвращает - list[str]
def split_words(text: str) -> list[str]:
    words = re.findall(r"[^\W_]+", text)
    return list(map(lambda word: word.lower(), words))


# Принимает - list[str]
# Возвращает - dict[str, int]
def count_word_frequencies(words: list[str]) -> dict[str, int]:
    return {
        word: sum(map(lambda item: item == word, words))
        for word in dict.fromkeys(words)
    }


# Принимает - dict[str, int]
# Возвращает - str или None
def top_word(freq: dict[str, int]) -> Optional[str]:
    if not freq:
        return None

    items = list(freq.items())

    def find_best(index: int, best: tuple[str, int]) -> tuple[str, int]:
        if index == len(items):
            return best

        current = items[index]
        better = current if current[1] > best[1] else best
        return find_best(index + 1, better)

    return find_best(1, items[0])[0]


# ============ Проверка работы функций ============

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


# ============ Рефлексия ============

# 1. Побочных эффектов нет:
#    - функции ничего не выводят на экран и не записывают в файлы;
#    - не используют внешнее состояние;
#    - не изменяют входные данные;
#    - не изменяют переданный список words.
#
# 2. Функции детерминированы:
#    при одинаковых аргументах они возвращают одинаковый результат.
#
# 3. Пустая строка:
#    split_words("") -> []
#
# 4. Пустой словарь:
#    top_word({}) -> None
