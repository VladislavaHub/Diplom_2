import allure

import response_message
from api_stellar_burgers import ApiStellarBurgers


class TestGettingOrdersFromAPerson:

    @allure.title('Получение заказов авторизованным пользоватем')
    def test_get_orders_auth_user(self, registration_user):
        response = ApiStellarBurgers.get_order_auth_user(registration_user[2])
        assert response.status_code == 200 and response_message.TRUE in response.text

    @allure.title('Получение заказов неавторизованного пользователя')
    def test_get_orders_no_auth_user(self):
        response = ApiStellarBurgers.get_order_no_auth_user()
        assert response.status_code == 401 and response_message.ERROR_NO_AUTHORIZATION in response.text
