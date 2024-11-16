import pytest


@pytest.fixture
def mock_vacancies():
    return [
        {
            "id": "111025345",
            "name": "Шеф-повар",
            "salary": {"from": 8000000, "to": 15000000, "currency": "UZS"},
            "url": "https://example.com/vacancy/111025345",
            "snippet": {
                "responsibility": "Координация работы поваров и другого кухонного персонала."
            }
        },
        {
            "id": "111025346",
            "name": "Помощник повара",
            "salary": None,
            "url": "https://example.com/vacancy/111025346",
            "snippet": {
                "responsibility": "Поддержка шеф-повара, помощь в приготовлении блюд."
            }
        },
    ]