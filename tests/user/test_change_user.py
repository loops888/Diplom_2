import pytest

import response_constants
from helpers import *


class TestChangeUser:
    @allure.title('Проверка успешного изменения пользователя.')
    @allure.description('Если пользователь авторизован - изменение его инфо успешно.')
    @pytest.mark.parametrize('update_data', [({'email': faker.email()}),
                                      ({'password': faker.password()}),
                                      ({'name': faker.name()})])
    def test_authorized_user_successful_change(self, update_data):
        data = {
            'email': faker.email(),
            'password': faker.password(),
            'name': faker.name()
        }
        register_user(data)
        login_response = login_user(data)
        token = login_response.json()['accessToken']
        change_response = change_user_info(token, update_data)
        delete_user(token)
        assert (
                change_response.status_code == 200
                and change_response.json()['success'] is True
        )

    @allure.title('Проверка ошибки при попытке изменения пользователя.')
    @allure.description('Если пользователь не авторизован - получаем ошибку.')
    @pytest.mark.parametrize('update_data', [({'email': faker.email()}),
                                             ({'password': faker.password()}),
                                             ({'name': faker.name()})])
    def test_not_authorized_user_unauthorized_error(self, update_data):
        change_response = change_user_info(token='Unauthorized', payload=update_data)
        assert (
                change_response.status_code == 401
                and change_response.json()['success'] is False
                and change_response.json()['message'] == response_constants.NOT_AUTHORIZED
        )
