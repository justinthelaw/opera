import pytest
from django.test import Client

def test_health_route():
    client = Client()
    response = client.get('/health')
    assert response.status_code == 200
    assert response.json() == {'status': 'ok'}
