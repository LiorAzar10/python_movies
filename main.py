def print_movies(movies: list[str]):
    print("movies list:\n")
    for i, m in enumerate(movies, 1):
        print(f"{i}. {m}")


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
        movies[movie] = ranking

    print_movies(movies.keys())


if __name__ == '__main__':
    main()
