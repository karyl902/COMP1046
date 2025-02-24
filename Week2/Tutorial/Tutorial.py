class Catalogue:
    def __init__(self):
        #self .movies = []
        self.movies = list()
        pass
    def add_movie(self, movie):
        self.movies.append(movie)
        return
    def search_by_name(self, name):
        for movie in self.movies:
            if movie in self.movies:
                return name
            pass
        return 
    pass
