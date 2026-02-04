class Book:
    def __init__(self, name, id, author):
        self.name = name
        self.id = id
        self.author = author
    def book(self):
        return f"Book's name : {self.name}, ID : {self.id}, Author : {self.author}"

class BookManangement:
    def __init__(self):
        self.library = []
    def addBook(self):
        name = input("Enter Book's name : ")
        id = input("Enter Book's ID : ")
        author = input("Enter Book's Author : ")
        book = Book(name, id, author)
        self.library.append(book)
    
    def displayBook(self):
        for e in self.library:
            print(e.name, " | ", e.id ," | ", e.author)
            print()
    def display_booklist(self):
        pass
    def search_for_book(self):
        InputID = input('Nhập ID sách: ')
        for n in self.library:
            if n[1] == InputID:
                print(n.name, " | ", n.id ," | ", n.author)

        pass
    def edit_book_information(self):
        pass
    def delete_book(self):
        pass
    def borrow_book(self):
        pass
    def return_book(self):
        pass
    def view_borrowed_book(self):
        pass
        
        




library=BookManangement()
library.library=[Book("book1", "ID1", "author1"),Book("book2", "ID2", "author2"),Book("book3", "ID3", "author3")]

library.displayBook()
