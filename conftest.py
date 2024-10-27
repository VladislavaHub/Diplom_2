import pytest

from data import Data
from api_stellar_burgers import ApiStellarBurgers


@pytest.fixture
def registration_user():
    registration_user_body = {"email": Data.EMAIL_FOR_REG, "password": Data.PASSWORD_FOR_REG, "name": Data.NAME_FOR_REG}
    login_body = {"email": Data.EMAIL_FOR_REG, "password": Data.PASSWORD_FOR_REG}
    response_reg = ApiStellarBurgers.registration_user(registration_user_body)
    token = response_reg.json()["accessToken"]
    yield [registration_user_body, login_body, token]
    ApiStellarBurgers.delete_user(token)