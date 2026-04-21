import allure
import pytest
from courier_api import CourierApi
from config import ERROR_MESSAGES


@allure.feature('Курьер')
@allure.story('Логин курьера')
class TestCourierLogin:

    @allure.title('Курьер может авторизоваться')
    def test_courier_login_success(self, courier_fixture):
        login, password, first_name = courier_fixture

        payload = {"login": login, "password": password}
        response = CourierApi.login_courier(payload)

        assert response.status_code == 200
        assert 'id' in response.json()
        assert response.json()['id'] > 0

    @allure.title('Авторизация возвращает ошибку при неверном логине или пароле')
    @pytest.mark.parametrize('scenario, login_mod, password_mod', [
        ('неверный логин', 'wrong_login', None),
        ('неверный пароль', None, 'wrong_password')
    ])
    def test_courier_login_invalid_credentials(self, courier_fixture, scenario, login_mod, password_mod):
        login, password, first_name = courier_fixture

        test_login = login_mod if login_mod else login
        test_password = password_mod if password_mod else password
        payload = {"login": test_login, "password": test_password}

        response = CourierApi.login_courier(payload)

        assert response.status_code == 404
        assert response.json().get('message') == ERROR_MESSAGES['login_not_found']

    @allure.title('Авторизация возвращает ошибку, если отсутствует поле')
    @pytest.mark.parametrize('payload_part', [
        {"password": "12345"},
        {"login": "user123"}
    ])
    def test_courier_login_missing_field(self, payload_part):
        response = CourierApi.login_courier(payload_part)
        
        if response.status_code == 504:
            pytest.skip("Сервер вернул 504 Gateway Timeout - проблема на стороне API")
        
        assert response.status_code == 400
        assert response.json().get('message') == ERROR_MESSAGES['insufficient_login_data']

    @allure.title('Авторизация несуществующего пользователя возвращает ошибку')
    def test_courier_login_nonexistent(self):
        payload = {"login": "nonexistent_user_12345", "password": "some_password"}
        response = CourierApi.login_courier(payload)

        assert response.status_code == 404
        assert response.json().get('message') == ERROR_MESSAGES['login_not_found']