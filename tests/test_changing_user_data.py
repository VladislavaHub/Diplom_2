import allure

import response_message
from data import Data
from api_stellar_burgers import ApiStellarBurgers


class TestChangingUserData:

    @allure.title('Успешное изменение данных пользователя c авторизацией')
    def test_change_data_auth_user(self, registration_user):
        ApiStellarBurgers.auth_user(registration_user[1])
        response = ApiStellarBurgers.change_user(registration_user[2], Data.DATA_CHANGE)
        assert response.status_code == 200 and response_message.TRUE in response.text

    @allure.title('Изменение данных пользователя без авторизации')
    def test_change_data_unauthorized_user(self, registration_user):
        response = ApiStellarBurgers.change_user_no_autorization(Data.DATA_CHANGE)
        assert response.status_code == 401 and response_message.ERROR_NO_AUTHORIZATION in response.text
