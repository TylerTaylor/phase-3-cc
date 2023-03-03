class Viewer:
    
    usernames = []

    def __init__(self, username):
        if (username not in Viewer.usernames):
            self.username = username
        else:
            raise Exception ("Username already exists")

        Viewer.usernames.append(self)
        
        self.reviewed_movies = []
        self.reviews = []


    # username property goes here!
    @property
    def username(self):
        return self._username

    @username.setter
    def username(self, username):
        if (5 < len(username) < 17) and (username not in Viewer.usernames):
           self._username = username
        else:
            raise Exception ("Ty Again please")
        
    # CHECKING FOR REVIEWED MOVIES

    def reviewed_movie(self, movie):
        if movie in self.reviewed_movies:
            return True
        else:
            return False

    # RATING NEW MOVIE

    def rate_movie(self, movie, rating):
        from lib.Review import Review
        Review(self, movie, rating)

        if movie in self.reviewed_movies:
            Review.rating = rating
        else:
            Review(self, movie, rating)
        
        

duane = Viewer("duanegrell")

print (duane.reviewed_movie("Up"))