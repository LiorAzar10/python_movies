from movie import Movie
from user_authenticate import UserAuthenticate
from user import User

END_COLOR = "\033[0m"
EXIT = "exit"


def print_movies(movies: list[str]):
    print("movies list:\n")
    for i, m in enumerate(movies, 1):
        print(f"{i}. {m}")


def print_ranking_stats(movies: dict[str, int]):
    rankings = movies.values()
    print(f"\033[31maverage ranking is {sum(rankings) / len(rankings)}" + END_COLOR)
    movie_with_max_value = max(movies, key=movies.get)
    print(f"\033[38;5;208mmovie with max ranking is: {movie_with_max_value}" + END_COLOR)
    movie_with_min_value = min(movies, key=movies.get)
    print(f"\033[95mmovie with min ranking is: {movie_with_min_value}" + END_COLOR)


def recommend_by_genre(movies: list[Movie], genre_list: list[str]):
    recommended_movies = [movie for movie in movies if movie.genre in genre_list]
    recommended_movies = sorted(recommended_movies, key=lambda x: -x.ranking)
    return recommended_movies


def ask_user_for_movies():
    movies = []

    while True:
        movie_name = input("enter movie name, exit to quit: ")
        if movie_name.strip().lower() == EXIT:
            break
        if movie_name in [movie.name for movie in movies]:
            print("movie already exist")
            continue
        ranking = int(input("enter movie ranking, from 1 to 10: "))
        genre = input("enter movie genre: ")
        movie = Movie(movie_name, ranking, genre)
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


def main():
    users = []
    while True:
        username = input("enter username, exit to break: ")
        if username.strip() == EXIT:
            break
        UserAuthenticate.login(username)

        movies = ask_user_for_movies()
        genres = ask_user_for_genres()

        user = User(username, movies, genres)
        users.append(user)


if __name__ == '__main__':
    main()
