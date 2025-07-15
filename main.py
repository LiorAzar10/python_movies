def print_movies(movies: list[str]):
    print("movies list:\n")
    for i, m in enumerate(movies, 1):
        print(f"{i}. {m}")


def print_ranking_stats(movies: dict[str, int]):
    rankings = movies.values()
    print(f"\033[31maverage ranking is {sum(rankings) / len(rankings)}\033[0m")
    movie_with_max_value = max(movies, key=movies.get)
    print(f"\033[38;5;208mmovie with max ranking is: {movie_with_max_value}\033[0m")
    movie_with_min_value = min(movies, key=movies.get)
    print(f"\033[95mmovie with min ranking is: {movie_with_min_value}\033[0m")


def main():
    movies = {}

    while True:
        movie = input("enter movie name, exit to quit: ")
        if movie.strip().lower() == "exit":
            break
        if movie in movies.keys():
            print("movie already exist")
            continue
        ranking = input("enter movie ranking, from 1 to 10: ")
        movies[movie] = int(ranking)

    print_ranking_stats(movies)


if __name__ == '__main__':
    main()
