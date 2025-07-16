from movie import Movie
from user_authenticate import UserAuthenticate
from user import User
from movie_database import MovieDatabase
from ui import UI

JSON_MOVIES_PATH = "./movies_data.json"
EXIT = "exit"


def recommend_by_genre(movies: list[Movie], genre_list: list[str]):
    recommended_movies = [movie for movie in movies if movie.genre in genre_list]
    recommended_movies = sorted(recommended_movies, key=lambda x: -x.ranking)
    return recommended_movies


def ask_user_for_movies(use_ranking=False):
    movies = []

    while True:
        movie_name = input("enter movie name, exit to quit: ")
        if movie_name.strip().lower() == EXIT:
            break
        if movie_name in [movie.name for movie in movies]:
            print("movie already exist")
            continue
        genre = input("enter movie genre: ")
        if use_ranking:
            ranking = int(input("enter movie ranking, from 1 to 10: "))
            movie = Movie(movie_name, genre, ranking)
        else:
            movie = Movie(movie_name, genre)
        movies.append(movie)
    return movies


def ask_user_for_genres():
    genres = []
    while True:
        genre = input("enter favourite genre, exit to quit: ")
        if genre.strip().lower() == EXIT:
            break
        genres.append(genre)

    return genres


def ask_for_users():
    users = []
    while True:
        username = input("enter username, exit to break: ")
        if username.strip() == EXIT:
            break

        password = input("enter password: ")

        movies = ask_user_for_movies(use_ranking=True)
        genres = ask_user_for_genres()

        user = User(username, movies, genres, password)
        users.append(user)
    return users


def main():
    movie_database = MovieDatabase(JSON_MOVIES_PATH)
    user = UserAuthenticate.login(movie_database, "lior", "lior123")
    movies = user.get_movie_names()
    UI.print_ranking_stats(user)


if __name__ == '__main__':
    main()
