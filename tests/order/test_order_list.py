import response_constants
from helpers import *


class TestOrderList:
    @allure.title('Проверка успешного получения списка заказов.')
    @allure.description('Если пользователь авторизован - выведется список его заказов.')
    def test_authorized_user_get_orders_list(self, generate_user_register_and_delete):
        token = generate_user_register_and_delete[1]
        orders_list_response = get_orders_list(token=token)
        assert (
                orders_list_response.status_code == 200
                and orders_list_response.json()['success'] is True
        )

    @allure.title('Проверка ошибки при получении списка заказов.')
    @allure.description('Если пользователь не авторизован - получим ошибку.')
    def test_unauthorized_user_unauthorized_error(self):
        orders_list_response = get_orders_list(token='Unauthorized')
        assert (
                orders_list_response.status_code == 401
                and orders_list_response.json()['message'] == response_constants.NOT_AUTHORIZED
        )
