import allure
import pytest
from courier_api import CourierApi
from order_api import OrderApi
from config import ERROR_MESSAGES
from data import ORDER_DATA_BLACK


@allure.feature('Заказы')
@allure.story('Принятие заказа')
class TestAcceptOrder:

    @allure.title('Успешное принятие заказа')
    def test_accept_order_success(self, courier_fixture, order_fixture):
        login, password, first_name = courier_fixture
        track = order_fixture
        
        # Получаем ID курьера
        courier_id = CourierApi.get_courier_id(login, password)
        
        # Получаем ID заказа по track
        order_response = OrderApi.get_order_by_track(track)
        order_id = order_response.json()['order']['id']

        response = OrderApi.accept_order(order_id, courier_id)

        assert response.status_code == 200
        assert response.json() == {"ok": True}

    @allure.title('Принятие заказа без ID курьера возвращает ошибку')
    def test_accept_order_no_courier_id(self, order_fixture):
        track = order_fixture
        
        order_response = OrderApi.get_order_by_track(track)
        order_id = order_response.json()['order']['id']

        response = OrderApi.accept_order(order_id, None)

        assert response.status_code == 400
        assert response.json().get('message') == ERROR_MESSAGES['insufficient_search_data']

    @allure.title('Принятие заказа с неверным ID курьера возвращает ошибку')
    def test_accept_order_invalid_courier_id(self, order_fixture):
        track = order_fixture
        
        order_response = OrderApi.get_order_by_track(track)
        order_id = order_response.json()['order']['id']

        response = OrderApi.accept_order(order_id, 999999)

        assert response.status_code == 404
        assert response.json().get('message') == "Курьера с таким id не существует"

    @allure.title('Принятие заказа с неверным ID заказа возвращает ошибку')
    def test_accept_order_invalid_order_id(self, courier_fixture):
        login, password, first_name = courier_fixture
        courier_id = CourierApi.get_courier_id(login, password)

        response = OrderApi.accept_order(999999, courier_id)

        assert response.status_code == 404
        assert response.json().get('message') == "Заказа с таким id не существует"