from carina import app
from fastapi.testclient import TestClient


client = TestClient(app)

def test_read_main():
    response = client.get("/healthcheck")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}