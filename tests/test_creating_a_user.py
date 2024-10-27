import allure
import pytest

import response_message
from data import Data
from api_stellar_burgers import ApiStellarBurgers


class TestCreatingAUser:

    @allure.title('Создание уникального пользователя')
    def test_registtration_new_user(self):
        response = ApiStellarBurgers.registration_user(Data.BODY_USER)
        token = response.json()["accessToken"]
        assert response.status_code == 200 and response_message.TRUE in response.text
        ApiStellarBurgers.delete_user(token)

    @allure.title('Создание пользователя, который уже зарегистрирован')
    def test_cannot_create_two_identical_user(self, registration_user):
        response = ApiStellarBurgers.registration_user(registration_user[0])
        assert response.status_code == 403 and response_message.ERROR_TWO_IDENTICAL_USER in response.text

    @allure.title('Создание пользователя и не заполнить одно из обязательных полей')
    @pytest.mark.parametrize('data', Data.DATA_FOR_REG)
    def test_mandatory_fields(self, data):
        response = ApiStellarBurgers.registration_user(data)
        assert response.status_code == 403 and response_message.ERROR_FAILED_ADD_NEW_USER == response.text
