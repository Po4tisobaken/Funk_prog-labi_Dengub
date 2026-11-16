from dataclasses import dataclass  # Создаёт класс для хранения данных.
from enum import Enum  # Задаёт набор именованных вариантов.
from typing import Generic, TypeVar, Union  # Параметры типов и их объединение.

# Уровень 1. Один из трёх вариантов состояния.
class LoadState(Enum):
    LOADING = "loading"
    SUCCESS = "success"
    ERROR = "error"


# Уровень 2. Имя, возраст и email хранятся вместе.
@dataclass(frozen=True)  # Поля объекта нельзя переназначить.
class User:
    name: str
    age: int
    email: str


# Уровень 3. Результат содержит либо значение, либо ошибку.
T = TypeVar("T")  # Тип успешного значения.
E = TypeVar("E")  # Тип ошибки.


@dataclass(frozen=True)
class Success(Generic[T]):  # Generic позволяет подставить нужный тип T.
    value: T


@dataclass(frozen=True)
class Failure(Generic[E]):  # Хранит ошибку типа E.
    error: E


Result = Union[Success[T], Failure[E]]  # Либо Success, либо Failure.


# Чистая: не меняет users, ошибку возвращает как значение, без исключения.
def make_result(users: list[User]) -> Result[list[User], str]:
    """Возвращает пользователей или понятное сообщение об ошибке."""
    if not users:
        return Failure("Список пользователей пуст")
    return Success(users.copy())  # Создаём новый список с теми же пользователями.


# Чистая: всегда одинаковые данные, без обращения к файлам и сети.
def load_users() -> Result[list[User], str]:
    """Чистая имитация загрузки: каждый вызов создаёт один и тот же список."""
    users = [
        User("Анна", 20, "anna@example.com"),
        User("Иван", 25, "ivan@example.com"),
        User("Мария", 31, "maria@example.com"),
    ]
    return make_result(users)


# Проверка работы. Вывод находится за пределами чистых функций.
state = LoadState.LOADING
print("Начальное состояние:", state.value)
result = load_users()

if isinstance(result, Success):  # Проверяем, какой вариант результата получен.
    state = LoadState.SUCCESS
    print("Состояние:", state.value)
    print("Пользователи:")
    for user in result.value:
        print(f"- {user.name}, {user.age} лет, {user.email}")
else:
    state = LoadState.ERROR
    print("Состояние:", state.value)
    print("Ошибка:", result.error)

print("\nПроверка пустого списка:")
print(make_result([]))


# Уровень 4. Рефлексия:
# LoadState имеет 3 значения: LOADING, SUCCESS и ERROR.
# У Result есть 2 конструктора: Success и Failure.
# Мощность суммы складывается из мощностей её вариантов:
# |Result[list[User], str]| = |list[User]| + |str|.
# В математической модели конечные строки, целые числа и конечные списки
# дают счётно бесконечное множество значений Result. Два варианта результата
# не означают, что у него всего два возможных значения.
#
# User создан через @dataclass(frozen=True), поэтому его поля нельзя изменить
# после создания объекта.
#
# Функции не читают файлы, не используют время или сеть и не меняют исходный
# список пользователей. При одинаковых аргументах они возвращают одинаковый
# результат.
# make_result([]) возвращает Failure, а не выбрасывает исключение.
# Настоящая сеть была бы побочным эффектом, поэтому здесь загрузка имитируется.
