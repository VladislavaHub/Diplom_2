import allure

import response_message
from data import Data
from api_stellar_burgers import ApiStellarBurgers


class TestCreatingAnOrder:

    @allure.title('Создание заказа c авторизацией и с указанием ингридиентов')
    def test_creating_order_auth_user(self, registration_user):
        ApiStellarBurgers.auth_user(registration_user[1])
        response_id = ApiStellarBurgers.get_ingedients()
        id_ingredient = response_id.json()['data'][3]
        response = ApiStellarBurgers.creating_order_ingredient(id_ingredient)
        assert response.status_code == 200 and response_message.TRUE in response.text
    @allure.title('Создание заказа без авторизации и с указанием ингридиентов')
    def test_creating_order_no_auth_user(self):
        response_id = ApiStellarBurgers.get_ingedients()
        id_ingredient = response_id.json()['data'][2]
        response = ApiStellarBurgers.creating_order_ingredient(id_ingredient)
        assert response.status_code == 200 and response_message.TRUE in response.text

    @allure.title('Создание заказа без ингредиентов')
    def test_creating_order_no_ingredients(self):
        response = ApiStellarBurgers.creating_order_no_ingredient()
        assert response.status_code == 400 and response_message.ERROR_INGREDIENT_CREATING_ODER in response.text

    @allure.title('Создание заказа с неверным хешем ингредиента')
    def test_creating_order_incorrect_hash_ingredient(self):
        response = ApiStellarBurgers.creating_order_ingredient(Data.INVALID_HASH_INGREDIENT)
        assert response.status_code == 500
