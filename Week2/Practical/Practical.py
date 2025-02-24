class Movie:
    def __init__(self, name, genre, minutes, rating):
        self.name = name
        self.genre = genre
        self.minutes = minutes
        self.rating = rating
action = Movie("Last Action Hero", "Action", 130, 'PG')
print(action)
# OUTPUT>>> <__main__.Movie object at 0x01BA1FB8>
