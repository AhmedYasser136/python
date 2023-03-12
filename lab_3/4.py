class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        
    def display(self):
        print("Title:", self.title)
        print("Author:", self.author)

# create a Book instance
book = Book("the atomic habits ", "jamesclear")

# display the book's title and author
book.display()
