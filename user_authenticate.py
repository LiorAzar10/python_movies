from user import User


class UserAuthenticate:
    @staticmethod
    def login(movie_database, username, password) -> User:
        users = movie_database.get_users()
        user = [user for user in users if (user.username == username and user.password == password)]
        if len(user) == 0:
            raise ValueError("user not found")
        print(f"connected as {username}")
        return user[0]

    @staticmethod
    def sign_up(movie_database, username, password):
        movie_database.add_user(username, password)
