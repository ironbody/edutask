import pytest
import unittest.mock as mock

from src.controllers.usercontroller import UserController

@pytest.mark.lab1
@pytest.mark.unit
def test_getUser_exist_valid():
    mockedDao = mock.MagicMock()

    mockedDao.find.return_value = [{'email': "test@test.com"}]

    controller = UserController(mockedDao)

    result = controller.get_user_by_email("test@test.com")

    assert result == {'email': "test@test.com"}

@pytest.mark.lab1
@pytest.mark.unit
def test_getUser_nonexist_valid():
    mockedDao = mock.MagicMock()

    mockedDao.find.return_value = []

    controller = UserController(mockedDao)

    result = controller.get_user_by_email("test@test.com")

    assert result == None

@pytest.mark.lab1
@pytest.mark.unit
def test_getUser_nonexist_invalid():
    mockedDao = mock.MagicMock()

    mockedDao.find.return_value = []

    controller = UserController(mockedDao)

    with pytest.raises(ValueError):
        controller.get_user_by_email("test.com")    
