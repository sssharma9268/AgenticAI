from fastapi.testclient import TestClient
from starlette import status

from app.main import app

client = TestClient(app)


def test_version_api() -> None:
    """Test the version API endpoint"""
    response = client.get("/api/version")
    assert response.status_code == status.HTTP_200_OK
    assert "version" in response.json()
    assert isinstance(response.json()["version"], str)


def test_version_check() -> None:
    response = client.get("/api/version")
    assert response.status_code == status.HTTP_200_OK
