class Library_item:
    def __init__(self, title , availability = True):
        self.title = title
        self.availability = availability
    
    def get_details(self):
        return f"Title: {self.title}, Availability: {'Available' if self.availability else 'Not Available'}"
    
class Book(Library_item):
    def __init__(self, title, author, genre, isbn, availability = True):
        self.author = author
        self.genre = genre
        self.isbn = isbn
        super().__init__(title, availability)
        
    def checkout(self):
        if self.availability:
            self.availability = False
            return f"Book {self.title} checked out."
        else:
            return f"Book {self.title} is not available, it has already been checked out."
        
    def return_book(self):
        self.availability = True
        return f"Book {self.title} returned."
    
    def update_availability(self, new_status):
        if not new_status and not self.availability:
            print("Book is currently checked out")
        else:
            self.availability = new_status
            
    def get_details(self):
        details = super().get_details()
        return (f"{details} Author: {self.author} Genre: {self.genre} isbn: {self.isbn}")
        
    def add_to_library(self):
        return (f"Book added to library: {self.title}")
        
book01 = Book("The First Song ", "Nicolas Sparks", "Romance", "342984")
book02 = Book("Ugly Love", "Collen Hover", "Romance", "98232")

print(book01.get_details())
print(book01.checkout())
print(book01.return_book())

print(book02.add_to_library())
print(book02.get_details())
print(book02.add_to_library())
