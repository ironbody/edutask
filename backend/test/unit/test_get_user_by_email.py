import pytest
import unittest.mock as mock

from src.controllers.usercontroller import UserController


@pytest.mark.lab1
@pytest.mark.unit
def test_case_1():
    mockedDao = mock.MagicMock()

    mockedDao.find.return_value = [{'email': "test@test.com",
                                    "firstName": "test",
                                    "lastName": "tester"}]

    controller = UserController(mockedDao)

    result = controller.get_user_by_email("test@test.com")

    assert result == {'email': "test@test.com",
                      "firstName": "test",
                      "lastName": "tester"}

@pytest.mark.lab1
@pytest.mark.unit
def test_case_2():
    mockedDao = mock.MagicMock()

    mockedDao.find.return_value = [{'email': "test@test.com",
                                    "firstName": "test1",
                                    "lastName": "tester"},
                                    {'email': "test@test.com",
                                    "firstName": "test2",
                                    "lastName": "tester"},]

    controller = UserController(mockedDao)

    result = controller.get_user_by_email("test@test.com")

    assert result == {'email': "test@test.com",
                      "firstName": "test1",
                      "lastName": "tester"}


@pytest.mark.lab1
@pytest.mark.unit
def test_case_3():
    mockedDao = mock.MagicMock()

    mockedDao.find.return_value = []

    controller = UserController(mockedDao)

    result = controller.get_user_by_email("test@test.com")

    assert result == None


@pytest.mark.lab1
@pytest.mark.unit()
@pytest.mark.parametrize('email',["test.com"])
def test_case_4(email):
    mockedDao = mock.MagicMock()

    mockedDao.find.return_value = []

    controller = UserController(mockedDao)

    with pytest.raises(ValueError):
        controller.get_user_by_email(email)

@pytest.mark.lab1
@pytest.mark.unit()
@pytest.mark.parametrize('email',["test@test.com"])
def test_case_5_to_7(email):
    mockedDao = mock.MagicMock()

    mockedDao.find.return_value = Exception

    controller = UserController(mockedDao)

    with pytest.raises(Exception):
        controller.get_user_by_email(email)

@pytest.mark.lab1
@pytest.mark.unit()
@pytest.mark.parametrize('email',["test.com"])
def test_case_5_to_7(email):
    mockedDao = mock.MagicMock()

    mockedDao.find.return_value = Exception

    controller = UserController(mockedDao)

    with pytest.raises(ValueError):
        controller.get_user_by_email(email)
