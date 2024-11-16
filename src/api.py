import requests
from abc import ABC, abstractmethod
from typing import List, Dict, Any


class AbstractAPI(ABC):
    """Абстрактный класс для работы с API."""

    @abstractmethod
    def connect(self):
        """Приватный метод для подключения к API."""
        pass

    @abstractmethod
    def get_vacancies(self, keyword: str) -> List[Dict[str, Any]]:
        """Метод для получения вакансий по ключевому слову."""
        pass


class HH(AbstractAPI):
    """Класс для работы с API HeadHunter."""

    def __init__(self, file_worker, filename: str = 'vacancies.json'):
        self._url = 'https://api.hh.ru/vacancies'
        self._headers = {'User-Agent': 'HH-User-Agent'}
        self._params = {'text': '', 'page': 0, 'per_page': 100}
        self._vacancies = []
        self.file_worker = file_worker
        self.filename = filename

    def connect(self):
        """Метод для установки соединения с API и проверки состояния сервиса."""
        response = requests.get(self._url, headers=self._headers)
        if response.status_code == 200:
            print("Соединение с API успешно установлено.")
        else:
            print(f"Ошибка подключения: {response.status_code}")

    def get_vacancies(self, keyword: str) -> List[Dict[str, Any]]:
        """Получение вакансий по ключевому слову"""
        self._params['text'] = keyword
        self._vacancies = []  # Сброс перед загрузкой
        self.connect()  # Проверяем соединение при выполнении запроса
        while self._params['page'] < 20:
            response = requests.get(self._url, headers=self._headers, params=self._params)
            if response.status_code == 200:
                items = response.json().get('items', [])
                self._vacancies.extend(items)
                if not items:  # Если нет больше вакансий
                    break
                self._params['page'] += 1
            else:
                print(f"Ошибка при запросе вакансий: {response.status_code}")
                break
        return self._vacancies
