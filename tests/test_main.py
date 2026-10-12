from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_health():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


def test_index_serves_html():
    response = client.get("/")
    assert response.status_code == 200
    assert "text/html" in response.headers["content-type"]


def test_profile_has_name():
    response = client.get("/api/profile")
    assert response.status_code == 200
    assert response.json()["name"]


def test_projects_is_a_list():
    response = client.get("/api/projects")
    assert response.status_code == 200
    assert isinstance(response.json(), list)
    assert all("name" in p for p in response.json())
