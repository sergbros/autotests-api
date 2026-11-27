import pytest
from _pytest.fixtures import SubRequest


@pytest.mark.parametrize("number", [1, 2, 3, -1])  # Параметризируем тест
# Название "number" в декораторе "parametrize" и в аргументах автотеста должны совпадать
def test_numbers(number: int):
    assert number > 0


@pytest.mark.parametrize("number, expected", [(1, 1), (2, 4), (3, 9)])
# В данном случае в качестве данных используется список с кортежами
def test_several_numbers(number: int, expected: int):
    # Возводим число number в квадрат и проверяем, что оно равно ожидаемому
    assert number ** 2 == expected


@pytest.mark.parametrize("os", ["macos", "windows", "linux", "debian"])  # Параметризируем по операционной системе
@pytest.mark.parametrize("host", [
    "https://dev.company.com",
    "https://stable.company.com",
    "https://prod.company.com"
])  # Параметризируем по хосту
def test_multiplication_of_numbers(os: str, host: str):
    assert len(os + host) > 0  # Проверка указана для примера


@pytest.fixture(params=[  # Параметризация фикстур
    "https://dev.company.com",
    "https://prod.company.com",
    "https://dev.company.com"
])
def host(request: SubRequest) -> str:
    return request.param


def test_host(host: str):
    print(f"Running test on host: {host}")


@pytest.mark.parametrize("user", ["Alice", "Bob", "Charlie"])
class TestOperations:
    def test_user_with_operation(self, user: str):
        print(f"User with operations: {user}")

    def test_user_without_operation(self, user: str):
        print(f"User without operations: {user}")


@pytest.mark.parametrize(
    "phone_number",
    ["+70000000011", "+70000000012", "+70000000013"],
    ids=[  # текстовые пояснения для параметров
        "User with money on bank account",
        "User without money on bank account",
        "User without operations on bank account"
    ]
)
def test_identifiers(phone_number: str):
    pass


users = {  # текстовые пояснения для параметров через словарь (ключ-значение)
    "+70000000011": "User with money on bank account",
    "+70000000012": "User without money on bank account",
    "+70000000013": "User without operations on bank account"
}


@pytest.mark.parametrize(
    "phone_number",
    users.keys(),
    ids=lambda phone_number: f"{phone_number}: {users[phone_number]}",
)
def test_identifiers_2(phone_number: str):
    pass


@pytest.mark.parametrize(
    "value",
    [1, pytest.param(2, marks=pytest.mark.skip(reason="Not supported")), 3]  # пример пропуска теста
)
def test_skip_example(value):
    pass


@pytest.mark.parametrize(
    "input_value",
    [
        pytest.param(1, marks=pytest.mark.xfail(reason="Known issue with 1")),
        2,
        pytest.param(3, marks=pytest.mark.skip(reason="Feature not implemented for 3")),
    ]
)
def test_xfail_function(input_value):
    assert input_value != 1
