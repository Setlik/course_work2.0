import json

from src.api import HH

from src.file_worker import JSONFileWorker


def user_interaction():
    """Функция для взаимодействия с пользователем."""
    file_worker = JSONFileWorker()
    parser = HH(file_worker)

    keyword = input("Введите ключевое слово для поиска вакансий: ")
    vacancies = parser.get_vacancies(keyword)

    if vacancies:
        n = int(input("Введите количество топ N вакансий по зарплате: "))

        # Сортируем вакансии по зарплате
        vacancies_sorted = sorted(vacancies, key=lambda x: (
                (x.get('salary', {}).get('from', 0) if isinstance(x.get('salary'), dict) else 0) or 0), reverse=True)

        # Получаем топ N вакансий
        top_vacancies = vacancies_sorted[:n]


        # Выводим топ N вакансий в консоль
        for i, vacancy in enumerate(top_vacancies, start=1):
            description = vacancy.get('snippet', {}).get('responsibility', 'Нет описания')

            print(f"{i}. {vacancy.get('name', 'Нет названия')}")
            print(f"   Зарплата: {vacancy.get('salary', {}).get('from', 0)}")
            print(f"   Ссылка: {vacancy.get('url', 'Нет ссылки')}")
            print(f"   Описание: {description}\n")

        # Сохраняем топ N вакансий в файл
        file_worker.save(top_vacancies)

        print(f"Топ {n} вакансий по зарплате сохранены в файл.")
    else:
        print("Вакансии не найдены.")



    # print(json.dumps(vacancies, indent=4, ensure_ascii=False))

if __name__ == "__main__":

    user_interaction()
