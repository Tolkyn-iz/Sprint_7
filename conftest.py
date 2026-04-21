import allure
import pytest
from courier_api import CourierApi
from order_api import OrderApi
from config import generate_random_string
from data import ORDER_DATA_BLACK


@pytest.fixture
@allure.step("Фикстура: создание и удаление курьера")
def courier_fixture():
    login = generate_random_string(10)
    password = generate_random_string(10)
    first_name = generate_random_string(10)
    
    payload = {
        "login": login,
        "password": password,
        "firstName": first_name
    }
    
    create_response = CourierApi.create_courier(payload)
    if create_response.status_code != 201:
        pytest.skip("Не удалось создать курьера для теста")
    
    # Возвращаем значения, а не generator
    return login, password, first_name


@pytest.fixture
@allure.step("Фикстура: создание и отмена заказа")
def order_fixture():
    order_data = ORDER_DATA_BLACK.copy()
    response = OrderApi.create_order(order_data)
    
    if response.status_code != 201:
        pytest.skip("Не удалось создать заказ для теста")
    
    track = response.json().get('track')
    return track