import pytest
from helpers import *


@allure.step('Создаем данные для курьера, передаем их, после чего удаляем его.')
@pytest.fixture
def generate_user_and_delete():
    data = generate_info_for_registration()
    registration_info = [data[0], data[1], data[2]]

    yield registration_info

    payload = {
        'email': data[0],
        'password': data[1],
        'name': data[2]
    }
    login_response = login_user(payload)
    token = login_response.json()['accessToken']
    delete_user(token)


@allure.step('Создаем данные для курьера, регистрируем, после чего удаляем его.')
@pytest.fixture
def generate_user_register_and_delete():
    data = generate_info_for_registration()

    payload = {
        'email': data[0],
        'password': data[1],
        'name': data[2]
    }
    registration_response = register_user(payload)
    registration_info = []
    if registration_response.status_code == 200:
        registration_info.append(data[0])
        registration_info.append(data[1])
        registration_info.append(data[2])

    yield registration_info

    payload = {
        'email': data[0],
        'password': data[1]
    }
    login_response = login_user(payload)
    token = login_response.json()['accessToken']
    delete_user(token)
