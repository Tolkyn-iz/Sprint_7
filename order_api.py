import allure
from api_client import ApiClient
from config import ORDERS_ENDPOINT, ACCEPT_ORDER_ENDPOINT, GET_ORDER_ENDPOINT, CANCEL_ORDER_ENDPOINT

class OrderApi:
    """Класс с методами для работы с заказами"""
    
    @staticmethod
    @allure.step("Создать заказ")
    def create_order(order_data):
        return ApiClient.post(ORDERS_ENDPOINT, json=order_data)
    
    @staticmethod
    @allure.step("Получить список заказов")
    def get_orders_list():
        return ApiClient.get(ORDERS_ENDPOINT)
    
    @staticmethod
    @allure.step("Принять заказ")
    def accept_order(order_id, courier_id):
        return ApiClient.put(f"{ACCEPT_ORDER_ENDPOINT}/{order_id}", params={'courierId': courier_id})
    
    @staticmethod
    @allure.step("Отменить заказ")
    def cancel_order(track):
        return ApiClient.put(CANCEL_ORDER_ENDPOINT, params={'track': track})
    
    @staticmethod
    @allure.step("Получить заказ по track номеру")
    def get_order_by_track(track):
        return ApiClient.get(GET_ORDER_ENDPOINT, params={'t': track})