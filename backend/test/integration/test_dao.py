import pytest
import unittest.mock as mock
from unittest.mock import patch

from src.util.dao import DAO

@pytest.fixture
@patch('src.util.dao.DAO', autospec=True)
