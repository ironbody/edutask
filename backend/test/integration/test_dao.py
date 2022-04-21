import pytest
from pymongo.errors import WriteError

from src.util.dao import DAO

@pytest.fixture
def dao():
    dao = DAO("test")
    dao.create({
        "required_string": "test",
        "required_bool": False,
        "items": ["3","4"],
    })

    yield dao
    dao.drop()


@pytest.mark.lab1
@pytest.mark.integration
def test_allValid(dao):
    data = {
        "required_string": "test",
        "required_bool": False,
        "items": ["1","2"],
    }
    result = dao.create(data)

    assert result["required_string"] == data["required_string"] and result["required_bool"] == data["required_bool"] and result["items"] == data["items"]


@pytest.mark.lab1
@pytest.mark.integration
def test_notUniqueItems(dao):
    data = {
        "required_string": "Test1",
        "required_bool": False,
        "items": ["3","4"],
    }
    
    with pytest.raises(WriteError):
        dao.create(data)

@pytest.mark.lab1
@pytest.mark.integration
def test_invalidBSON(dao):
    data = {
        "required_string": True,
        "required_bool": "test",
        "items": ["1","2"],
    }

    with pytest.raises(WriteError):
        dao.create(data)

@pytest.mark.lab1
@pytest.mark.integration
def test_invalidBSON_notUniqueItems(dao):
    data = {
        "required_string": "true",
        "required_bool": "test",
        "items": ["3","4"],
    }

    with pytest.raises(WriteError):
        dao.create(data)

@pytest.mark.lab1
@pytest.mark.integration
def test_none_valid(dao):
    data = {
        "required_bool": "test",
        "items": ["3","4"],
    }

    with pytest.raises(WriteError):
        dao.create(data)

@pytest.mark.lab1
@pytest.mark.integration
def test_invalidRequired(dao):
    data = {
        "required_bool": True,
        "items": ["1","2"]
    }
    
    with pytest.raises(WriteError):
        dao.create(data)

@pytest.mark.lab1
@pytest.mark.integration
def test_invalidRequired_notUniqueItems(dao):
    data = {
        "required_string": "Test1",
        "items": ["3","4"]
    }

    with pytest.raises(WriteError):
        dao.create(data)

@pytest.mark.lab1
@pytest.mark.integration
def test_invalidRequired_invalidBSON(dao):
    data = {
        "required_bool": "test",
        "items": ["1","2"],
    }
    
    with pytest.raises(WriteError):
        dao.create(data)