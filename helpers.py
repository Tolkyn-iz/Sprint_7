import requests
import random
import string

BASE_URL = 'https://qa-scooter.praktikum-services.ru'


def generate_random_string(length):
    """Генерирует случайную строку из букв нижнего регистра"""
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(length))


def register_new_courier_and_return_login_password():
    """Регистрирует нового курьера, возвращает логин, пароль и имя"""
    login = generate_random_string(10)
    password = generate_random_string(10)
    first_name = generate_random_string(10)

    payload = {
        "login": login,
        "password": password,
        "firstName": first_name
    }

    response = requests.post(f'{BASE_URL}/api/v1/courier', data=payload)

    if response.status_code == 201:
        return login, password, first_name
    return None, None, None


def create_order_and_return_track(order_data=None):
    """Создаёт заказ и возвращает его track номер"""
    if order_data is None:
        order_data = {
            "firstName": "Тест",
            "lastName": "Тестов",
            "address": "Москва, ул. Тестовая, 1",
            "metroStation": 4,
            "phone": "+79998887766",
            "rentTime": 5,
            "deliveryDate": "2024-12-31",
            "comment": "Тестовый заказ",
            "color": ["BLACK"]
        }

    response = requests.post(f'{BASE_URL}/api/v1/orders', json=order_data)

    if response.status_code == 201:
        return response.json().get('track')
    return None