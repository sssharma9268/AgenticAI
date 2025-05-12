from fastapi.testclient import TestClient
from starlette import status

from app.main import app

client = TestClient(app)


def test_health_check_without_auth() -> None:
    """Test health check endpoint without required headers"""
    response = client.get("/api/health")
    assert response.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY


def test_health_check_with_auth() -> None:
    """Test health check endpoint with valid headers"""
    headers = {"app-id": "test-app", "api-key": "test-key"}
    response = client.get("/api/health", headers=headers)

    assert response.status_code == status.HTTP_200_OK
    data = response.json()
    assert "status" in data
    assert data["status"] == "ok"
    assert "app_id" in data
    assert data["app_id"] == "test-app"
