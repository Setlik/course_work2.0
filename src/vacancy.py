class Vacancy:
    """Класс для представления вакансии."""

    __slots__ = ('title', 'url', 'salary', 'description')

    def __init__(self, title: str, url: str, salary: float, description: str):
        self.title = title
        self.url = url
        self.salary = salary if self.validate_salary(salary) else 0.0
        self.description = description

    def validate_salary(self, salary: float) -> bool:
        """Валидация значения зарплаты."""
        return salary >= 0

    def __lt__(self, other):
        """Сравнение по зарплате меньше."""
        return self.salary < other.salary

    def __gt__(self, other):
        """Сравнение по зарплате больше."""
        return self.salary > other.salary
