class Movie:
    def __init__(self, name, genre, ranking=None):
        self.name = name
        self.genre = genre
        self.ranking = ranking

    def __str__(self):
        return f"movie name : {self.name}, genre: {self.genre}"
