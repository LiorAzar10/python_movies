from movie import Movie

END_COLOR = "\033[0m"


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


def main():
    movies = []

    while True:
        movie_name = input("enter movie name, exit to quit: ")
        if movie_name.strip().lower() == "exit":
            break
        if movie_name in [movie.name for movie in movies]:
            print("movie already exist")
            continue
        ranking = input("enter movie ranking, from 1 to 10: ")
        genre = input("enter movie genre: ")
        movie = Movie(movie_name, ranking, genre)
        movies.append(movie)


if __name__ == '__main__':
    main()
