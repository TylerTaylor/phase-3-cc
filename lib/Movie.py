class Movie:
    
    def __init__(self, title):
        self.title = title

        self.reviews = []
        self.reviewers = []

    # title property goes here!
    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, title):
        if type(title) == str and len(title) > 0:
            self._title = title
        else:
            raise Exception ("need a string please")

    @classmethod
    def average_rating(self):
        return sum ([review.rating for review in self.reviews]) / len(self.reviews)

    @classmethod
    def highest_rated(cls):
        max_rating = max (review.rating for review in cls.reviews)
        if cls.review.rating == max_rating: 
            max_movie = cls.title

        return max ()


lion_king = Movie("Lion King")

print(lion_king.title)
