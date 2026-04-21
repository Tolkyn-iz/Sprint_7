import allure
import requests
from config import BASE_URL

class ApiClient:
    """Класс для инкапсуляции HTTP запросов"""
    
    @staticmethod
    @allure.step("Отправить POST запрос на {endpoint}")
    def post(endpoint, data=None, json=None, params=None):
        url = f"{BASE_URL}{endpoint}"
        response = requests.post(url, data=data, json=json, params=params)
        allure.attach(str(response.status_code), name="Status Code", attachment_type=allure.attachment_type.TEXT)
        return response
    
    @staticmethod
    @allure.step("Отправить GET запрос на {endpoint}")
    def get(endpoint, params=None):
        url = f"{BASE_URL}{endpoint}"
        response = requests.get(url, params=params)
        allure.attach(str(response.status_code), name="Status Code", attachment_type=allure.attachment_type.TEXT)
        return response
    
    @staticmethod
    @allure.step("Отправить PUT запрос на {endpoint}")
    def put(endpoint, params=None, json=None):
        url = f"{BASE_URL}{endpoint}"
        response = requests.put(url, params=params, json=json)
        allure.attach(str(response.status_code), name="Status Code", attachment_type=allure.attachment_type.TEXT)
        return response
    
    @staticmethod
    @allure.step("Отправить DELETE запрос на {endpoint}")
    def delete(endpoint):
        url = f"{BASE_URL}{endpoint}"
        response = requests.delete(url)
        allure.attach(str(response.status_code), name="Status Code", attachment_type=allure.attachment_type.TEXT)
        return response