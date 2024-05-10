import response_constants
from helpers import *


class TestCreateOrder:
    @allure.title('Проверка ошибки заказа без ингредиентов.')
    @allure.description('Если пользователь не авторизован и не добавил ингредиенты - получим ошибку.')
    def test_unauthorized_user_without_ingredients_no_ingredients_error(self):
        order_response = create_order(token='Unauthorized', ids=None)
        assert (
                order_response.status_code == 400
                and order_response.json()['success'] is False
                and order_response.json()['message'] == response_constants.NO_INGREDIENTS
        )
    @allure.title('Проверка успешного создания заказа с ингредиентами.')
    @allure.description('Если не авторизованный пользователь добавил ингредиенты - заказ создается.')
    def test_unauthorized_user_with_ingredients_order_created(self):
        ingredients = get_ingredients()
        order_response = create_order(token='Unauthorized', ids=ingredients)
        assert (
                order_response.status_code == 200
                and order_response.json()['success'] is True
            )

    @allure.title('Проверка ошибки заказа без ингредиентов.')
    @allure.description('Если пользователь авторизован и не добавил ингредиенты - получим ошибку.')
    def test_authorized_user_without_ingredients_no_ingredients_error(self, generate_user_register_and_delete):
        data = {
            'email': generate_user_register_and_delete[0],
            'password': generate_user_register_and_delete[1],
            'name': generate_user_register_and_delete[2]
        }
        login_response = login_user(data)
        token = login_response.json()['accessToken']
        order_response = create_order(token=token, ids=None)
        assert (
                order_response.status_code == 400
                and order_response.json()['success'] is False
                and order_response.json()['message'] == response_constants.NO_INGREDIENTS
        )

    @allure.title('Проверка успешного создания заказа с ингредиентами.')
    @allure.description('Если авторизованный пользователь добавил ингредиенты - заказ создается.')
    def test_authorized_user_with_ingredients_order_created(self, generate_user_register_and_delete):
        data = {
            'email': generate_user_register_and_delete[0],
            'password': generate_user_register_and_delete[1],
            'name': generate_user_register_and_delete[2]
        }
        login_response = login_user(data)
        token = login_response.json()['accessToken']
        ingredients = get_ingredients()
        order_response = create_order(token=token, ids=ingredients)
        assert (
                order_response.status_code == 200
                and order_response.json()['success'] is True
        )

    @allure.title('Проверка ошибки заказа с неверным хешем ингредиентов.')
    @allure.description('Если авторизованный пользователь добавил неверный хеш - получаем ошибку.')
    def test_authorized_user_with_incorrect_hex_order_created(self, generate_user_register_and_delete):
        data = {
            'email': generate_user_register_and_delete[0],
            'password': generate_user_register_and_delete[1],
            'name': generate_user_register_and_delete[2]
        }
        login_response = login_user(data)
        token = login_response.json()['accessToken']
        ingredients = generate_random_hex_24()
        order_response = create_order(token=token, ids=ingredients)
        assert (
                order_response.status_code == 400
                and order_response.json()['success'] is False
                and order_response.json()['message'] == response_constants.INCORRECT_INGREDIENT
        )
