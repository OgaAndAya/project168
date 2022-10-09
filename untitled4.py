class Book:
    def __init__(self,name,author,price,publish_year,):
        self.book_name = name
        self.book_author = author
        self.book_published= publish_year
        self.book_price = price
        
    def add_Book(self):
        print("Name: " + self.book_name)
        print("author: " + str(self.book_author))
        print("price: " + str(self.book_price))
        print("publish_year: " + self.book_published)
        print("book added")
        
book_1= Book("Bud not Buddy", "Christopher Paul Curtis", 8.99,"2002,January 8")
book_1.add_Book()

book_2= Book("The Lightning Theif","Rick Riordan", 6.99,"2010,Febuary 12")
book_2.add_Book()





