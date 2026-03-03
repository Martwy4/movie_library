import requests

API_TOKEN = "eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI2OWVmYTNhYzMyOWU0N2FjMzZhZDk4MTllY2U1NzE2NyIsIm5iZiI6MTc3MjIwNTMzNy4wNzEsInN1YiI6IjY5YTFiNTE5YTM1YWE1NWE1MGY1MmQ0YSIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.auBIUiTAOhz5_7zvs9460PObI5wcovC2u7YqD-KQqX0"

def get_popular_movies():
    url = "https://api.themoviedb.org/3/movie/popular?language=pl-PL"

    headers = {
        "Authorization": f"Bearer {API_TOKEN}",
        "accept": "application/json"
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json().get("results", [])
    else:
        return []

def get_movies(list_type):
    url = f"https://api.themoviedb.org/3/movie/{list_type}?language=pl-PL"

    headers = {
        "Authorization": f"Bearer {API_TOKEN}",
        "accept": "application/json"
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json().get("results", [])
    else:
        return []

def get_movie_details(movie_id):
    url = f"https://api.themoviedb.org/3/movie/{movie_id}?language=pl-PL"

    headers = {
        "Authorization": f"Bearer {API_TOKEN}",
        "accept": "application/json"
    }

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        return response.json()
    else:
        return None

def get_movie_credits(movie_id):
    url = f"https://api.themoviedb.org/3/movie/{movie_id}/credits"

    headers = {
        "Authorization": f"Bearer {API_TOKEN}",
        "accept": "application/json"
    }

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        return response.json().get("cast", [])
    else:
        return []

def get_poster_url(path, size="w500"):
    return f"https://image.tmdb.org/t/p/{size}{path}"