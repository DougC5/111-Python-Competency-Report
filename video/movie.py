
class Movie (object):
    movie_id = 0
    title = ''
    year = 0
    price = 0.0
    stock = 0

    def __init__ (self, movie_id, title, year, price, stock):
        self.movie_id = movie_id
        self.title = title
        self.year = year
        self.price = price
        self.stock = stock

        print('Im the constructor of the movie')
