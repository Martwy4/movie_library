import pytest
from app import app
from unittest.mock import Mock


@pytest.mark.parametrize(
    "list_type",
    ["popular", "top_rated", "upcoming", "now_playing"]
)
def test_homepage_lists(monkeypatch, list_type):
    api_mock = Mock(return_value=[])

    monkeypatch.setattr("tmdb.get_movies", api_mock)

    with app.test_client() as client:
        response = client.get(f"/?list={list_type}")

        assert response.status_code == 200
        api_mock.assert_called_once_with(list_type)


def test_homepage_default_list(monkeypatch):
    api_mock = Mock(return_value=[])

    monkeypatch.setattr("tmdb.get_movies", api_mock)

    with app.test_client() as client:
        response = client.get("/")

        assert response.status_code == 200
        api_mock.assert_called_once_with("popular")


def test_homepage_invalid_list(monkeypatch):
    api_mock = Mock(return_value=[])

    monkeypatch.setattr("tmdb.get_movies", api_mock)

    with app.test_client() as client:
        response = client.get("/?list=wrong_list")

        assert response.status_code == 200
        api_mock.assert_called_once_with("popular")