from unittest import result
import pytest
import unittest.mock as mock
from unittest.mock import patch

from src.util.dao import DAO

@pytest.fixture
def user_dao():
    dao = DAO("user")
    yield dao
    dao.drop()


@pytest.mark.lab1
@pytest.mark.integration
def test_test(user_dao):
    data = {
        "firstName": "test",
        "email": "test@test.com",
    }
    result = user_dao.create(data)

    assert (result["firstName"] == data["firstName"] and result["email"] == data["email"])