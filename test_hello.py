from fastapi.testclient import TestClient
from app import app

client = TestClient(app)

def test_valid_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"msg": "Aloha Men :::::::::!)"}

def test_valid_check():
    response = client.get("/check")
    assert response.status_code == 200
    assert response.json() == {"msg": "Hello World"}
