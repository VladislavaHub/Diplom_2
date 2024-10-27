import generators


class Data:
    EMAIL_FOR_REG = generators.generated_email()
    PASSWORD_FOR_REG = generators.generated_password()
    NAME_FOR_REG = generators.generated_name()

    BODY_USER = {"email": EMAIL_FOR_REG, "password": PASSWORD_FOR_REG, "name": NAME_FOR_REG}

    DATA_WRONG = {'email': 'Vlada.2000@yandex.ru', 'password': '1234'}

    DATA_CHANGE = {'email': 'Vlada.2000@yandex.ru', "password": '12345', "name": 'Vlada'}

    DATA_FOR_REG = [{'password': generators.generated_password(), 'firstname': generators.generated_name()},
                    {'email': generators.generated_email(), 'firstname': generators.generated_name()}]

    INVALID_HASH_INGREDIENT = '0'