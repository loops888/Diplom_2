import response_constants
from helpers import *


class TestLoginUser:
    @allure.title('Проверка успешной авторизации пользователя.')
    @allure.description('Если переданы данные существующего юзера - логин успешен.')
    def test_correct_user_successful_login(self, generate_user_register_and_delete):
        data = {
            'email': generate_user_register_and_delete[0],
            'password': generate_user_register_and_delete[1]
        }
        response = login_user(data)
        assert (
                response.status_code == 200
                and response.json()['success'] is True
        )

    @allure.title('Проверка провальной авторизации пользователя.')
    @allure.description('Если неверно передан имейл - получим ошибку.')
    def test_incorrect_email_unauthorized(self, generate_user_register_and_delete):
        data = {
            'email': f'{generate_user_register_and_delete[0]}{5}',
            'password': generate_user_register_and_delete[1]
        }
        response = login_user(data)
        assert (
                response.status_code == 401
                and response.json()['success'] is False
                and response.json()['message'] == response_constants.INCORRECT_INFO_LOGIN
        )

    @allure.title('Проверка провальной авторизации пользователя.')
    @allure.description('Если неверно передан пароль - получим ошибку.')
    def test_incorrect_password_unauthorized(self, generate_user_register_and_delete):
        data = {
            'email': generate_user_register_and_delete[0],
            'password': f'{generate_user_register_and_delete[1]}{"pass"}'
        }
        response = login_user(data)
        assert (
                response.status_code == 401
                and response.json()['success'] is False
                and response.json()['message'] == response_constants.INCORRECT_INFO_LOGIN
        )
