import json
import os
from movie import Movie
from user import User


class MovieDatabase:
    def __init__(self, filepath):
        self.filepath = filepath
        self.data = self.load_data()

    def load_data(self):
        if os.path.exists(self.filepath):
            with open(self.filepath, "r") as f:
                return json.load(f)
        else:
            return {"users": [], "movies": []}

    def save_data(self):
        with open(self.filepath, "w") as f:
            json.dump(self.data, f, indent=2)

    def get_users(self):
        users_dicts = self.data["users"]
        users = [User(**user_dict) for user_dict in users_dicts]
        for user in users:
            user.movies = [Movie(**movie_dict) for movie_dict in user.movies]
        return users

    def add_user(self, user: User):
        self.data["users"].append({
            "username": user.username,
            "movies": [movie.__dict__ for movie in user.movies],
            "genres": [genre for genre in user.genres],
            "password": user.password
        })

        self.save_data()

    def get_movies(self):
        movies_dicts = self.data["movies"]
        return [Movie(**movie_dict) for movie_dict in movies_dicts]

    def add_movie(self, movie: Movie):
        self.data["movies"].append({
            "name": movie.name,
            "genre": movie.genre
        })

        self.save_data()
