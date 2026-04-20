import pytest
import requests
from helpers import register_new_courier_and_return_login_password, create_order_and_return_track

BASE_URL = 'https://qa-scooter.praktikum-services.ru'


@pytest.fixture
def create_courier_and_delete():
    """Фикстура создаёт курьера, возвращает его данные и удаляет после теста"""
    login, password, first_name = register_new_courier_and_return_login_password()
    payload = {"login": login, "password": password}
    yield login, password, first_name

    # Удаляем курьера после теста
    response = requests.post(f'{BASE_URL}/api/v1/courier/login', data=payload)
    if response.status_code == 200:
        courier_id = response.json().get('id')
        if courier_id:
            requests.delete(f'{BASE_URL}/api/v1/courier/{courier_id}')


@pytest.fixture
def create_order():
    """Фикстура создаёт заказ и возвращает его track номер"""
    track = create_order_and_return_track()
    yield track

    # Отмена заказа после теста (опционально, если API поддерживает)
    if track:
        try:
            requests.put(f'{BASE_URL}/api/v1/orders/cancel', params={'track': track})
        except:
            pass