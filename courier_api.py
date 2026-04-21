import allure
from api_client import ApiClient
from config import COURIER_ENDPOINT, LOGIN_ENDPOINT

class CourierApi:
    """Класс с методами для работы с курьером"""
    
    @staticmethod
    @allure.step("Создать курьера")
    def create_courier(payload):
        return ApiClient.post(COURIER_ENDPOINT, data=payload)
    
    @staticmethod
    @allure.step("Авторизовать курьера")
    def login_courier(payload):
        return ApiClient.post(LOGIN_ENDPOINT, data=payload)
    
    @staticmethod
    @allure.step("Удалить курьера")
    def delete_courier(courier_id):
        return ApiClient.delete(f"{COURIER_ENDPOINT}/{courier_id}")
    
    @staticmethod
    @allure.step("Получить ID курьера по логину и паролю")
    def get_courier_id(login, password):
        response = CourierApi.login_courier({"login": login, "password": password})
        if response.status_code == 200:
            return response.json().get('id')
        return None