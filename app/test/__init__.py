# '''Init the client'''
import pytest
from app import app

@pytest.fixture(scope="module", autouse=True)
def client():
    '''Test app start or not'''
    client = app.test_client()
    client.URL_API_PREFIX = '/api/v1'
    yield client  