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


def ask_for_users():
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
    return users


def main():
    users = [User("lior", [Movie("movie1", 9, "comedy")], ["comedy"]),
             User("lior2", [Movie("movie1", 9, "comedy"), Movie("movie3", 10, "comedy")], ["drama", "comedy"]),
             User("lior3", [Movie("movie1", 9, "comedy"), Movie("movie4", 6, "drama")], ["drama", "comedy"])]

    username = input("enter username: ")
    UserAuthenticate.login(username)
    current_user = [user for user in users if users if user.name == username][0]
    similar_users = [user for user in users if current_user.has_joined_movies(user) and user.name != username]
    for user in similar_users:
        print(f"loved movies by {user.name}:")
        for movie in user.movies:
            if movie.name not in current_user.get_movie_names():
                print(movie)


if __name__ == '__main__':
    main()
