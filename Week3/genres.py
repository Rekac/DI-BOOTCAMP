
from inheritance import Book
import os 

class Fiction(Book):
    def __init__(self, title, author, publication_date, price):
        super().__init__(title, author, publication_date, price)
        self.genre = 'Fiction'
        




book2 = Fiction('Contact', 'Carl Sagan', 1995, 150)
book2.present()

book3 = Fiction('Fifty Shades of Grey', 'E.L. James', 2010, 5)
book3.present()