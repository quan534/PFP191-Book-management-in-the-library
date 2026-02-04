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
        book = BookData()
