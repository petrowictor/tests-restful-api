import allure

@allure.step("Check that response status code equals to {expected}")
def assert_status_code(actual: int, expected: int):
    """
    Проверяет, что HTTP-статус ответа соответствует ожидаемому.

    :param: actual (int): Фактический статус-код.
    :param: expected (int): Ожидаемый статус-код.
    :raises: AssertionError: Если статус-коды не совпадают.
    """
    assert actual == expected, (
        f'Incorrect response status code. '
        f'Expected status code: {expected}. '
        f'Actual status code: {actual}'
    )