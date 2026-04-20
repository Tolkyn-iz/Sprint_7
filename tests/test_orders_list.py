import allure
import requests

BASE_URL = 'https://qa-scooter.praktikum-services.ru'


@allure.feature('Заказы')
@allure.story('Список заказов')
class TestOrdersList:

    @allure.title('Получение списка заказов возвращает массив')
    def test_get_orders_list_returns_array(self):
        response = requests.get(f'{BASE_URL}/api/v1/orders')

        assert response.status_code == 200
        assert 'orders' in response.json()
        assert isinstance(response.json()['orders'], list)