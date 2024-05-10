import pytest

import response_constants
from helpers import *


class TestCreateUser:
    @allure.title('Проверка успешной регистрации пользователя.')
    @allure.description('Если переданы уникальные данные для регистрации - пользователь создается успешно.')
    def test_random_data_new_user_created(self, generate_user_and_delete):
        data = {
            'email': generate_user_and_delete[0],
            'password': generate_user_and_delete[1],
            'name': generate_user_and_delete[2]
        }
        response = register_user(data)
        assert (
                response.status_code == 200
                and response.json()['success'] is True
        )

    @allure.title('Проверка провальной регистрации пользователя.')
    @allure.description('Если переданы данные пользователя, который уже зарегистрирован - регистрация не пройдет.')
    def test_existing_user_user_already_exists(self, generate_user_register_and_delete):
        data = {
            'email': generate_user_register_and_delete[0],
            'password': generate_user_register_and_delete[1],
            'name': generate_user_register_and_delete[2]
        }
        response = register_user(data)
        assert (
                response.status_code == 403
                and response.json()['success'] is False
                and response.json()['message'] == response_constants.EXISTED_USER_REGISTRATION
        )

    @allure.title('Проверка провальной регистрации пользователя.')
    @allure.description('Если не заполнено одно из обязательных полей - регистрация не пройдет.')
    @pytest.mark.parametrize('data', [({'email': 'youshallnotpass@gmail.com',
                                        'password': 'youshallnotpassword',
                                        'name': ''}),
                                      ({'email': '',
                                        'password': 'youshallnotpassword',
                                        'name': 'youshallnotpassname'}),
                                      ({'email': 'youshallnotpass@gmail.com',
                                        'password': '',
                                        'name': 'youshallnotpassname'}),
                                      ({'email': '',
                                        'password': '',
                                        'name': ''})
                                      ])
    def test_empty_necessary_fields_not_enough_data(self, data):
        response = register_user(data)
        assert (
                response.status_code == 403
                and response.json()['success'] is False
                and response.json()['message'] == response_constants.NOT_ENOUGH_INFO_REGISTRATION
        )
