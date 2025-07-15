def print_movies(movies: list[str]):
    print("movies list:\n")
    for i, m in enumerate(movies, 1):
        print(f"{i}. {m}")


def main():
    movies = []

    while True:
        movie = input("enter movie name, exit to quit: ")
        if movie.strip().lower() == "exit":
            break
        movies.append(movie)

    print_movies(movies)


if __name__ == '__main__':
    main()
