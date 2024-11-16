def test_get_vacancies(mock_vacancies):
    expected_names = ["Шеф-повар", "Помощник повара"]
    assert [vacancy['name'] for vacancy in mock_vacancies] == expected_names


def test_vacancy_salary():
    vacancy = {
        "id": "111025345",
        "name": "Шеф-повар",
        "salary": {"from": 8000000, "to": 15000000, "currency": "UZS"},
        "url": "https://example.com/vacancy/111025345",
        "snippet": {
            "responsibility": "Координация работы поваров и другого кухонного персонала."
        }
    }
    salary_from = vacancy.get('salary', {}).get('from', 0)
    assert salary_from == 8000000


def test_vacancy_description(mock_vacancies):
    vacancy = mock_vacancies[0]
    description = vacancy.get('snippet', {}).get('responsibility', 'Нет описания')
    assert description == "Координация работы поваров и другого кухонного персонала."


def test_no_salary():
    vacancy = \
        {
            "id": "111025346",
            "name": "Помощник повара",
            "salary": None,
            "url": "https://example.com/vacancy/111025346",
            "snippet": {
                "responsibility": "Поддержка шеф-повара, помощь в приготовлении блюд."
            }
        }
    salary_from = (vacancy.get('salary') or {}).get('from', 0)
    assert salary_from == 0
