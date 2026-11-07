from litestar.testing import TestClient

from lite_star_app.app import app


def test_hello() -> None:
    with TestClient(app=app) as client:
        response = client.get("/")

    assert response.status_code == 200
    assert response.json() == {"message": "Hello, world!"}
