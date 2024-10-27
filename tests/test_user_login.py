import allure

import response_message
from api_stellar_burgers import ApiStellarBurgers
from data import Data


class TestUserLogin:

    @allure.title('Логин под существующим пользователем')
    def test_auth_existing_user(self, registration_user):
        response = ApiStellarBurgers.auth_user(registration_user[1])
        assert response.status_code == 200 and response_message.TRUE in response.text

    @allure.title('Логин с неверным логином и паролем')
    def test_wrong_login_and_password(self, registration_user):
        response = ApiStellarBurgers.auth_user(Data.DATA_WRONG)
        assert response.status_code == 401 and response_message.ERROR_WRONG_USER_DATA == response.text
