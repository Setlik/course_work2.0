from abc import ABC, abstractmethod
from typing import List, Dict, Any
import json
import os


class AbstractFileWorker(ABC):
    """Абстрактный класс для работы с файлами."""

    @abstractmethod
    def load(self) -> List[Dict[str, Any]]:
        """Метод для загрузки данных из файла."""
        pass

    @abstractmethod
    def save(self, data: List[Dict[str, Any]]):
        """Метод для сохранения данных в файл."""
        pass


class JSONFileWorker(AbstractFileWorker):
    """Класс для работы с JSON-файлом."""

    def __init__(self, filename: str = 'data/vacancies.json'):
        self._filename = filename
        self._data = []

    def load(self) -> List[Dict[str, Any]]:
        """Загрузка данных из JSON-файла."""
        if os.path.exists(self._filename):
            with open(self._filename, 'r') as f:
                self._data = json.load(f)
        return self._data

    def save(self, data: List[Dict[str, Any]]):
        """Сохранение данных в JSON-файл."""
        existing_data = self.load()
        existing_titles = {item['title'] for item in existing_data}

        for item in data:
            # Проверка наличия 'name' и 'salary' в элементе
            if 'name' in item:
                title = item['name']
                if title not in existing_titles:
                    salary = item.get('salary')  # Получаем словарь зарплаты
                    salary_from = salary.get('from', 0) if salary is not None else 0
                    description = item.get('snippet', {}).get('requirement', '')

                    existing_data.append({
                        'title': title,
                        'url': item.get('url', ''),
                        'salary': salary_from,
                        'description': description
                    })

        with open(self._filename, 'w') as f:
            json.dump(existing_data, f)
