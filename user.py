from movie import Movie


class User:
    def __init__(self, name: str, movies: list[Movie], recommended_genres: list[str]):
        self.name = name
        self.movies = movies
        self.recommended_genres = recommended_genres

    def get_movie_names(self):
        return [movie.name for movie in self.movies]

    def has_joined_movies(self, other):
        other_movie_names = other.get_movie_names()
        if set(self.get_movie_names()) & set(other_movie_names):
            return True
        return False
