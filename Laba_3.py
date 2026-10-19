from dataclasses import dataclass
from enum import Enum
from typing import Generic, TypeVar, Union


class LoadState(Enum):
    LOADING = "loading"
    SUCCESS = "success"
    ERROR = "error"


@dataclass(frozen=True)
class User:
    name: str
    age: int
    email: str


T = TypeVar("T")
E = TypeVar("E")


@dataclass(frozen=True)
class Success(Generic[T]):
    value: T


@dataclass(frozen=True)
class Failure(Generic[E]):
    error: E


Result = Union[Success[T], Failure[E]]


def make_result(users: list[User]) -> Result[list[User], str]:
    """Возвращает пользователей или понятное сообщение об ошибке."""
    if not users:
        return Failure("Список пользователей пуст")
    return Success(users.copy())


def load_users() -> Result[list[User], str]:
    """Имитация загрузки списка пользователей."""
    users = [
        User("Анна", 20, "anna@example.com"),
        User("Иван", 25, "ivan@example.com"),
        User("Мария", 31, "maria@example.com"),
    ]
    return make_result(users)


# Сначала данные загружаются, поэтому состояние — LOADING.
state = LoadState.LOADING
result = load_users()

if isinstance(result, Success):
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


# Рефлексия:
# LoadState имеет 3 значения: LOADING, SUCCESS и ERROR.
# У Result есть 2 конструктора: Success и Failure.
# Самих значений Result бесконечно много, потому что список пользователей
# и текст ошибки могут содержать разное количество вариантов.
#
# User создан через @dataclass(frozen=True), поэтому его поля нельзя изменить
# после создания объекта.
#
# Функции не читают файлы, не используют время или сеть и не меняют исходный
# список пользователей. При одинаковых аргументах они возвращают одинаковый
# результат.
