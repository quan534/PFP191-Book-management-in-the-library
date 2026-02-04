class BookData:
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
        book = BookData(name, id, author)
        self.library.append(book)
    
    def displayBook(self):
        for e in self.library:
            print(e.name, " | ", e.id ," | ", e.author)
            print()
        




library=BookManangement()
library.library=[BookData("book1", "ID1", "author1"),BookData("book2", "ID2", "author2"),BookData("book3", "ID3", "author3")]

library.displayBook()