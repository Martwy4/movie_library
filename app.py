from flask import Flask, render_template, request
import tmdb

app = Flask(__name__)

MOVIE_LISTS = {
    "popular": "Popularne",
    "top_rated": "Najwyżej oceniane",
    "upcoming": "Nadchodzące",
    "now_playing": "Teraz grane"
}

@app.context_processor
def utility_processor():
    return {
        "tmdb_image_url": tmdb.get_poster_url
    }

@app.route("/")
def homepage():
    selected_list = request.args.get("list", "popular")
    movies = tmdb.get_movies(selected_list)[:8]
    if selected_list not in MOVIE_LISTS:
        selected_list = "popular"

    return render_template(
        "homepage.html",
        movies=movies,
        movie_lists=MOVIE_LISTS,
        selected_list=selected_list
    )

@app.route("/movie/<int:movie_id>")
def movie_details(movie_id):
    movie = tmdb.get_movie_details(movie_id)
    cast = tmdb.get_movie_credits(movie_id)[:4] 

    if movie is None:
        return "Film nie istnieje", 404
    return render_template("movie_details.html", movie=movie,cast=cast)

if __name__ == "__main__":
    app.run(debug=True)