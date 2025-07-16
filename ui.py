from movie import Movie
from user import User

END_COLOR = "\033[0m"


class UI:
    @staticmethod
    def print_movies(movies: list[str]):
        print("movies list:")
        for i, m in enumerate(movies, 1):
            print(f"{i}. {m}")

    @staticmethod
    def print_ranking_stats(user: User):
        movies_ranking_dict = {movie: movie.ranking for movie in user.movies}
        rankings = [movie.ranking for movie in user.movies]

        print(f"\033[31maverage ranking is {sum(rankings) / len(rankings)}" + END_COLOR)
        movie_with_max_value = max(movies_ranking_dict, key=movies_ranking_dict.get)
        print(f"\033[38;5;208mmovie with max ranking is: {movie_with_max_value}" + END_COLOR)
        movie_with_min_value = min(movies_ranking_dict, key=movies_ranking_dict.get)
        print(f"\033[95mmovie with min ranking is: {movie_with_min_value}" + END_COLOR)
