import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

import pytest  # noqa: E402

from app import app  # noqa: E402


@pytest.fixture()
def client():
    app.config.update(TESTING=True)
    return app.test_client()


def test_health(client):
    resp = client.get("/health")
    assert resp.status_code == 200
    assert resp.get_json() == {"status": "ok"}


def test_list_items(client):
    resp = client.get("/items")
    assert resp.status_code == 200
    assert len(resp.get_json()) == 3


def test_get_item(client):
    resp = client.get("/items/1")
    assert resp.status_code == 200
    assert resp.get_json()["name"] == "Widget"


def test_get_item_not_found(client):
    assert client.get("/items/999").status_code == 404
