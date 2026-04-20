import allure
import pytest
import requests
from helpers import generate_random_string, register_new_courier_and_return_login_password

BASE_URL = 'https://qa-scooter.praktikum-services.ru'


@allure.feature('Курьер')
@allure.story('Удаление курьера')
class TestCourierDelete:

    @allure.title('Успешное удаление курьера')
    def test_delete_courier_success(self):
        login, password, first_name = register_new_courier_and_return_login_password()
        if not login:
            pytest.skip("Не удалось создать курьера для теста")

        # Получаем ID курьера
        login_response = requests.post(f'{BASE_URL}/api/v1/courier/login', data={"login": login, "password": password})
        courier_id = login_response.json()['id']

        response = requests.delete(f'{BASE_URL}/api/v1/courier/{courier_id}')

        assert response.status_code == 200
        assert response.json() == {"ok": True}

    @allure.title('Удаление курьера без ID возвращает ошибку')
    def test_delete_courier_no_id(self):
        response = requests.delete(f'{BASE_URL}/api/v1/courier/')

        assert response.status_code == 404

    @allure.title('Удаление курьера с несуществующим ID возвращает ошибку')
    def test_delete_courier_invalid_id(self):
        response = requests.delete(f'{BASE_URL}/api/v1/courier/999999999')

        assert response.status_code == 404
        assert response.json().get('message') == "Курьера с таким id нет."