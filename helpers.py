import secrets

import allure
import requests

import url_constants
from faker import Faker

faker = Faker()


@allure.step('Генерируем рандомный хэш.')
def generate_random_hex_24():
    hex = secrets.token_hex(12)
    return hex


@allure.step('Генерируем данные для регистрации пользователя.')
def generate_info_for_registration():
    email = faker.email()
    password = faker.password()
    name = faker.name()
    return email, password, name


@allure.step('Отправляем запрос на регистрацию пользователя.')
def register_user(payload):
    request = requests.post(f'{url_constants.URL + url_constants.CREATE_USER}', json=payload)
    return request


@allure.step('Отправляем запрос на логин пользователя.')
def login_user(payload):
    request = requests.post(f'{url_constants.URL + url_constants.LOGIN_USER}', json=payload)
    return request


@allure.step('Отправляем запрос на удаление пользователя.')
def delete_user(token):
    headers = {
        "Authorization": token
    }
    request = requests.delete(f'{url_constants.URL + url_constants.INFO_USER}', headers=headers)
    return request


@allure.step('Отправляем запрос на получение информации о пользователе.')
def get_user_info(token):
    headers = {
        "Authorization": token
    }
    request = requests.get(f'{url_constants.URL + url_constants.INFO_USER}', headers=headers)
    return request


@allure.step('Отправляем запрос на обновление данных о пользователе.')
def change_user_info(token, payload):
    headers = {
        "Authorization": token
    }
    request = requests.patch(f'{url_constants.URL + url_constants.INFO_USER}', headers=headers, json=payload)
    return request


@allure.step('Отправляем запрос на получение данных об ингредиентах.')
def get_ingredients():
    request = requests.get(f'{url_constants.URL + url_constants.GET_INGREDIENTS}')
    ingredients = []
    for i in request.json()['data']:
        ingredients.append(i['_id'])
        return ingredients


@allure.step('Отправляем запрос на создание заказа.')
def create_order(token, ids):
    headers = {
        "Authorization": token
    }
    payload = {
        "ingredients": ids
    }
    request = requests.post(f'{url_constants.URL + url_constants.ORDERS}', headers=headers, json=payload)
    return request


@allure.step('Отправляем запрос на получение списка заказов.')
def get_orders_list(token):
    headers = {
        "Authorization": token
    }
    request = requests.get(f'{url_constants.URL + url_constants.ORDERS}', headers=headers)
    return request
