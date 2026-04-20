import allure
import pytest
import requests
from helpers import create_order_and_return_track

BASE_URL = 'https://qa-scooter.praktikum-services.ru'


@allure.feature('Заказы')
@allure.story('Получение заказа по номеру')
class TestGetOrderByTrack:

    @allure.title('Успешное получение заказа по track номеру')
    def test_get_order_by_track_success(self):
        track = create_order_and_return_track()
        if not track:
            pytest.skip("Не удалось создать заказ")

        response = requests.get(f'{BASE_URL}/api/v1/orders/track', params={'t': track})

        assert response.status_code == 200
        assert 'order' in response.json()
        assert response.json()['order']['track'] == track

        # Очистка
        requests.put(f'{BASE_URL}/api/v1/orders/cancel', params={'track': track})

    @allure.title('Запрос без номера заказа возвращает ошибку')
    def test_get_order_no_track(self):
        response = requests.get(f'{BASE_URL}/api/v1/orders/track')

        assert response.status_code == 400
        assert response.json().get('message') == "Недостаточно данных для поиска"

    @allure.title('Запрос с несуществующим номером заказа возвращает ошибку')
    def test_get_order_invalid_track(self):
        response = requests.get(f'{BASE_URL}/api/v1/orders/track', params={'t': 999999999})

        assert response.status_code == 404
        assert response.json().get('message') == "Заказ не найден"