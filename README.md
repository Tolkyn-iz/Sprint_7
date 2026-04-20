# Sprint_7 - Тестирование API учебного сервиса qa-scooter

## Описание проекта
Проект содержит автоматические тесты для API учебного сервиса [qa-scooter](https://qa-scooter.praktikum-services.ru/).

## Документация API
[Документация API](https://qa-scooter.praktikum-services.ru/docs/)

## Технологии
- Python 3.9+
- pytest
- requests
- Allure

## Структура проекта
Sprint_7/
├── tests/ # Директория с тестами
│ ├── test_courier_creation.py # Тесты создания курьера
│ ├── test_courier_login.py # Тесты логина курьера
│ ├── test_create_order.py # Тесты создания заказа
│ ├── test_orders_list.py # Тесты списка заказов
│ ├── test_courier_delete.py # Тесты удаления курьера (доп. задание)
│ ├── test_accept_order.py # Тесты принятия заказа (доп. задание)
│ └── test_get_order_by_track.py # Тесты получения заказа по номеру (доп. задание)
├── conftest.py # Фикстуры
├── helpers.py # Вспомогательные функции
├── data.py # Тестовые данные
├── requirements.txt # Зависимости
├── .gitignore # Исключения для Git
└── README.md # Описание проекта