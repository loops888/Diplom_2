import pytest
from helpers import *


@allure.step('Создаем данные для курьера, передаем их, после чего удаляем его.')
@pytest.fixture
def generate_user_and_delete():
    payload = generate_info_for_registration()
    yield payload

    login_response = login_user(payload)
    token = login_response.json()['accessToken']
    delete_user(token)


@allure.step('Создаем данные для курьера, регистрируем, после чего удаляем его.')
@pytest.fixture
def generate_user_register_and_delete():
    payload = generate_info_for_registration()
    register_user(payload)
    login_response = login_user(payload)
    token = login_response.json()['accessToken']
    yield payload, token

    delete_user(token)
