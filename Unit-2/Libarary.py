#Develop a library class that has instance like book_name,author,and availability status. The class should provide methods to check out a book, return a book, and check the availability of a book. 


class Library:
    def __init__(self, book_name, author):
        self.book_name = book_name
        self.author = author
        self.is_available = True

    def check_out(self):
        if self.is_available:
            self.is_available = False
            return f"You have checked out '{self.book_name}' by {self.author}."
        else:
            return f"'{self.book_name}' is currently not available."

    def return_book(self):
        if not self.is_available:
            self.is_available = True
            return f"You have returned '{self.book_name}'"
        else:
            return f"'{self.book_name}' was not checked out."

    def check_availability(self):
        if self.is_available:
            return f"'{self.book_name}' by {self.author} is available."
        else:
            return f"'{self.book_name}' by {self.author} is currently not available." 
        

book1 = Library("Surrounded by Psychopaths", "Thomas Erikson")                                                              
print(book1.check_availability()) 
print(book1.check_out())          
print(book1.check_availability())  
print(book1.return_book())         
print(book1.check_availability())   

