import pytest
from pymongo.errors import WriteError

from src.util.dao import DAO

@pytest.fixture
def dao():
    dao = DAO("test")
    dao.create({
        "required_string": "test2",
        "required_bool": False,
    })

    yield dao
    dao.drop()


@pytest.mark.lab1
@pytest.mark.integration
def test_1(dao):
    data = {
        "required_string": "test",
        "required_bool": False,
    }
    result = dao.create(data)

    assert result["required_string"] == data["required_string"] and result["required_bool"] == data["required_bool"]

@pytest.mark.lab1
@pytest.mark.integration
def test_2(dao):
    data = {
        "required_string": "test2",
        "required_bool": True,
    }

    with pytest.raises(WriteError):
        dao.create(data)

@pytest.mark.lab1
@pytest.mark.integration
def test_3(dao):
    data = {
        "required_string": "test",
        "required_bool": "test",
    }

    with pytest.raises(WriteError):
        dao.create(data)

@pytest.mark.lab1
@pytest.mark.integration
def test_4(dao):
    data = {
        "required_bool": "test",
    }

    with pytest.raises(WriteError):
        dao.create(data)