class Book:
    def __init__(self, name, id, author, quantity):
        self.name = name
        self.id = id
        self.author = author
        self.quantity = quantity

    def __str__(self):
        return f"Book's name : {self.name}, ID : {self.id}, Author : {self.author}, Quanity : {self.quanity}"

class BookManangement:
    def __init__(self):
        self.library = []
        
    def addBook(self):
        name = input("Enter Book's name : ")
        id = input("Enter Book's ID : ")
        author = input("Enter Book's Author : ")
        quanity = int(input("Enter the number of books : ")
        book = Book(name, id, author,quantity)
        self.library.append(book)
        
    def displayBook(self):
        for e in self.library:
            print(e.name, " | ", e.id ," | ", e.author)

   
    def display_booklist(self):
        
        
    def search_for_book(self):
        InputID = input('Nhập ID sách: ')
        for n in self.library:
            if n[1] == InputID:
                print(n.name, " | ", n.id ," | ", n.author)
                
    def edit_book_information(self):
        pass
        
    def delete_book(self):
        removed_ID = input("Enter the removed book's ID : ")
        for book in self.library:
            if book.id == removed_ID:
                self.library.remove(book)
                break
    def borrow(self):
        self.borrow_count = 0
        if self.quantity = 0:
            raise ValueError('This book is currently not available')
        self.quantity -= 1
        self.borrow_count += 1
        
    def return_book(self):
        self.quantity +=1

    def find_book_by_id(self, id):
        for book in self.library:
            if book.id == id:
                return book
        return None
    def borrow_book(self,id):
        book = self.find_book_by_id(id)
        if book is None:
            print('Book not found')
            return
        book.borrow()
        print('Borrow successfully')
        print(book)
        
    def return_book(self):
        pass
    def view_borrowed_book(self):
        pass
        
        




library=BookManangement()
library.library=[Book("book1", "ID1", "author1"),Book("book2", "ID2", "author2"),Book("book3", "ID3", "author3")]

library.displayBook()






