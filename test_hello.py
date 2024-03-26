from fastapi.testclient import TestClient
from app import app

client = TestClient(app)

def test_valid_check():
    response = client.get("/metrics")
    assert response.status_code == 200
