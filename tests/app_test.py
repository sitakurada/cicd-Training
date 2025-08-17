import sys
import os

# Add parent directory (project root) to Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app import app

def test_home():
    client = app.test_client()
    response = client.get('/')
    assert response.status_code == 200
    assert b'Hello World' in response.data

def test_hello():
    client = app.test_client()
    response = client.get('/hello')
    assert response.status_code == 200
    assert b'Hello Mark' in response.data
