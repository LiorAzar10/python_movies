from movie import Movie


class User:
    def __init__(self, username: str, movies: list[Movie], genres: list[str], password: str):
        self.username = username
        self.movies = movies
        self.genres = genres
        self.password = password

    def get_movie_names(self):
        return [movie.name for movie in self.movies]

    def has_joined_movies(self, other):
        other_movie_names = other.get_movie_names()
        if set(self.get_movie_names()) & set(other_movie_names):
            return True
        return False
