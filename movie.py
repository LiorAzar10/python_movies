class Movie:
    def __init__(self, name, ranking=None, genre=None):
        self.name = name
        self.ranking = ranking
        self.genre = genre

    def __str__(self):
        return f"movie name : {self.name} with ranking of {self.ranking} and genre of {self.genre}"
