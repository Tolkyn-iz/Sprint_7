import allure
import pytest
import requests
from data import ORDER_DATA_BLACK, ORDER_DATA_GREY, ORDER_DATA_BOTH_COLORS, ORDER_DATA_NO_COLOR

BASE_URL = 'https://qa-scooter.praktikum-services.ru'


@allure.feature('Заказы')
@allure.story('Создание заказа')
class TestCreateOrder:

    @allure.title('Создание заказа с разными вариантами цвета')
    @pytest.mark.parametrize('order_data, description', [
        (ORDER_DATA_BLACK, 'только BLACK'),
        (ORDER_DATA_GREY, 'только GREY'),
        (ORDER_DATA_BOTH_COLORS, 'оба цвета'),
        (ORDER_DATA_NO_COLOR, 'без указания цвета')
    ])
    def test_create_order_with_colors(self, order_data, description):
        response = requests.post(f'{BASE_URL}/api/v1/orders', json=order_data)

        assert response.status_code == 201
        assert 'track' in response.json()
        assert isinstance(response.json()['track'], int)

        # Очистка: отмена заказа
        track = response.json()['track']
        requests.put(f'{BASE_URL}/api/v1/orders/cancel', params={'track': track})