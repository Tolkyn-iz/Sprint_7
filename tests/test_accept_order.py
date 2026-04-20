import allure
import pytest
import requests
from helpers import register_new_courier_and_return_login_password, create_order_and_return_track

BASE_URL = 'https://qa-scooter.praktikum-services.ru'


@allure.feature('Заказы')
@allure.story('Принятие заказа')
class TestAcceptOrder:

    @allure.title('Успешное принятие заказа')
    def test_accept_order_success(self):
        # Создаём курьера
        login, password, first_name = register_new_courier_and_return_login_password()
        if not login:
            pytest.skip("Не удалось создать курьера")

        # Получаем ID курьера
        login_response = requests.post(f'{BASE_URL}/api/v1/courier/login', data={"login": login, "password": password})
        courier_id = login_response.json()['id']

        # Создаём заказ
        track = create_order_and_return_track()
        if not track:
            pytest.skip("Не удалось создать заказ")

        # Получаем ID заказа по track
        order_response = requests.get(f'{BASE_URL}/api/v1/orders/track', params={'t': track})
        order_id = order_response.json()['order']['id']

        # Принимаем заказ
        response = requests.put(f'{BASE_URL}/api/v1/orders/accept/{order_id}', params={'courierId': courier_id})

        assert response.status_code == 200
        assert response.json() == {"ok": True}

        # Очистка
        requests.delete(f'{BASE_URL}/api/v1/courier/{courier_id}')

    @allure.title('Принятие заказа без ID курьера возвращает ошибку')
    def test_accept_order_no_courier_id(self):
        # Создаём заказ
        track = create_order_and_return_track()
        if not track:
            pytest.skip("Не удалось создать заказ")

        order_response = requests.get(f'{BASE_URL}/api/v1/orders/track', params={'t': track})
        order_id = order_response.json()['order']['id']

        response = requests.put(f'{BASE_URL}/api/v1/orders/accept/{order_id}')

        assert response.status_code == 400
        assert response.json().get('message') == "Недостаточно данных для поиска"

    @allure.title('Принятие заказа с неверным ID курьера возвращает ошибку')
    def test_accept_order_invalid_courier_id(self):
        track = create_order_and_return_track()
        if not track:
            pytest.skip("Не удалось создать заказ")

        order_response = requests.get(f'{BASE_URL}/api/v1/orders/track', params={'t': track})
        order_id = order_response.json()['order']['id']

        response = requests.put(f'{BASE_URL}/api/v1/orders/accept/{order_id}', params={'courierId': 999999})

        assert response.status_code == 404
        assert response.json().get('message') == "Курьера с таким id не существует"

    @allure.title('Принятие заказа без ID заказа возвращает ошибку')
    def test_accept_order_no_order_id(self):
        login, password, first_name = register_new_courier_and_return_login_password()
        if not login:
            pytest.skip("Не удалось создать курьера")

        login_response = requests.post(f'{BASE_URL}/api/v1/courier/login', data={"login": login, "password": password})
        courier_id = login_response.json()['id']

        response = requests.put(f'{BASE_URL}/api/v1/orders/accept/', params={'courierId': courier_id})

        assert response.status_code == 404

        requests.delete(f'{BASE_URL}/api/v1/courier/{courier_id}')