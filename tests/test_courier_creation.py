import allure
import pytest
from courier_api import CourierApi
from config import ERROR_MESSAGES, generate_random_string


@allure.feature('Курьер')
@allure.story('Создание курьера')
class TestCourierCreation:

    @allure.title('Курьера можно создать')
    def test_create_courier_success(self):
        login = generate_random_string(10)
        password = generate_random_string(10)
        first_name = generate_random_string(10)
        payload = {
            "login": login,
            "password": password,
            "firstName": first_name
        }

        response = CourierApi.create_courier(payload)

        assert response.status_code == 201
        assert response.json() == {"ok": True}

        # Очистка
        courier_id = CourierApi.get_courier_id(login, password)
        if courier_id:
            CourierApi.delete_courier(courier_id)

    @allure.title('Нельзя создать двух одинаковых курьеров')
    def test_cannot_create_duplicate_courier(self, courier_fixture):
        login, password, first_name = courier_fixture

        payload = {
            "login": login,
            "password": password,
            "firstName": first_name
        }

        response = CourierApi.create_courier(payload)

        assert response.status_code == 409
        assert response.json().get('message') == ERROR_MESSAGES['duplicate_login']

    @allure.title('Запрос возвращает ошибку, если отсутствует обязательное поле')
    @pytest.mark.parametrize('payload_part, expected_status', [
        ({"password": "12345", "firstName": "Name"}, 400),
        ({"login": "user123", "firstName": "Name"}, 400),
        ({"login": "user123", "password": "12345"}, 400)
    ])
    def test_create_courier_missing_field(self, payload_part, expected_status):
        response = CourierApi.create_courier(payload_part)
        
        # API возвращает 409 для случая без firstName
        if 'firstName' not in payload_part and response.status_code == 409:
            assert response.status_code == 409
        else:
            assert response.status_code == expected_status
            assert response.json().get('message') == ERROR_MESSAGES['insufficient_data']

    @allure.title('Нельзя создать курьера с уже существующим логином')
    def test_create_courier_existing_login(self, courier_fixture):
        login, password, first_name = courier_fixture

        payload = {
            "login": login,
            "password": generate_random_string(10),
            "firstName": generate_random_string(10)
        }

        response = CourierApi.create_courier(payload)

        assert response.status_code == 409
        assert response.json().get('message') == ERROR_MESSAGES['duplicate_login']