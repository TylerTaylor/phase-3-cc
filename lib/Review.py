from lib.Movie import Movie
from lib.Viewer import Viewer

class Review:
    
    def __init__(self, viewer, movie, rating):
        self.viewer = viewer
        self.movie = movie
        self.rating = rating

    # viewer property goes here!
    @property
    def viewer(self):
        return self._viewer

    @viewer.setter
    def viewer(self, viewer):
        if isinstance (viewer, Viewer):
            self._viewer = viewer
        else:
            raise Exception ("Try again please")

    # movie property goes here!
    @property
    def movie(self):
        return self._movie

    @movie.setter
    def movie(self, movie):
        if isinstance (movie, Movie):
            self._movie = movie
        else:
            raise Exception ("Try again please")

    # rating property goes here!
    @property
    def rating(self):
        return self._rating

    @rating.setter
    def rating(self, rating):
        if 0 < rating < 6:
            self._rating = rating
        else:
            raise Exception ("Need interger, 1-5")



# up = Review ("Duane", "Up", 5)

# print (up.rating)
# print (up.movie)
# print (up.viewer)

