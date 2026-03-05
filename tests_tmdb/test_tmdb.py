import tmdb
from unittest.mock import Mock


def test_get_movies_returns_list(monkeypatch):

    fake_response = Mock()
    fake_response.status_code = 200
    fake_response.json.return_value = {
        "results": [
            {"id": 1, "title": "Test Movie"}
        ]
    }

    def mock_get(*args, **kwargs):
        return fake_response

    monkeypatch.setattr(tmdb.requests, "get", mock_get)

    movies = tmdb.get_movies("popular")

    assert isinstance(movies, list)
    assert movies[0]["title"] == "Test Movie"


def test_get_movies_endpoint(monkeypatch):

    called_url = {}

    fake_response = Mock()
    fake_response.status_code = 200
    fake_response.json.return_value = {"results": []}

    def mock_get(url, headers=None):
        called_url["url"] = url
        return fake_response

    monkeypatch.setattr(tmdb.requests, "get", mock_get)

    tmdb.get_movies("popular")

    assert "movie/popular" in called_url["url"]


def test_get_movie_details(monkeypatch):

    fake_response = Mock()
    fake_response.status_code = 200
    fake_response.json.return_value = {
        "id": 550,
        "title": "Fight Club"
    }

    monkeypatch.setattr(
        tmdb.requests,
        "get",
        lambda *args, **kwargs: fake_response
    )

    movie = tmdb.get_movie_details(550)

    assert movie["title"] == "Fight Club"
    assert movie["id"] == 550


def test_get_movie_details_error(monkeypatch):

    fake_response = Mock()
    fake_response.status_code = 404

    monkeypatch.setattr(
        tmdb.requests,
        "get",
        lambda *args, **kwargs: fake_response
    )

    movie = tmdb.get_movie_details(999)

    assert movie is None