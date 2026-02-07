class Book:
    def __init__(self, name, id, author, quantity):
        self.name = name
        self.id = id
        self.author = author
        self.quantity = quantity
        self.borrow_count = 0
    def information(self):
        return f"Book's name : {self.name}, ID : {self.id}, Author : {self.author}"

    def is_available(self):
        return self.quantity>0

    def borrow(self):
        if not self.is_available():
            raise ValueError('This book is currently not available')
        self.quantity -= 1
        self.borrow_count += 1

    def return_book(self):
        self.quantity +=1

class BookManangement:
    def __init__(self):
        self.library = []
        
    def addBook(self):
        name = input("Enter Book's name : ")
        id = input("Enter Book's ID : ")
        author = input("Enter Book's Author : ")
        book = Book(name, id, author)
        self.library.append(book)
 #cho nay neu nhu k co sach thi co display gi ko ong   
    def displayBook(self):
        for e in self.library:
            print(e.name, " | ", e.id ," | ", e.author)

   
    def display_booklist(self):
        pass
        
class Book:
    def __init__(self, name, id, author, quantity):
        self.name = name
        self.id = id
        self.author = author
        self.quantity = quantity
        self.borrow_count = 0   
    def information(self):
        return f"Book's name : {self.name}, ID : {self.id}, Author : {self.author}, Quantity : {self.quantity}"

    def __str__(self):
        return f"Book's name : {self.name}, ID : {self.id}, Author : {self.author}"

class BookManangement:
    def __init__(self):
        self.library = []
        
    def addBook(self):
        name = input("Enter Book's name : ")
        id = input("Enter Book's ID : ")
        author = input("Enter Book's Author : ")
        quantity = int(input("Enter the number of books : "))
        book = Book(name, id, author,quantity)
        self.library.append(book)
        print("book added!")

 #cho nay neu nhu k co sach thi co display gi ko ong   
    def displayBook(self,book_id):
        book=self.find_book_by_id(book_id)
        if book == None:
            print("book not found!")
        else:
            book.information()

   
    def display_booklist(self):
        print("Name".ljust(35), " | ", "Id".ljust(5), " | ", "Author".ljust(20), " | ", "Quantity")
        print("-----------------------------------------------------------------------------------")
        for e in self.library:
            print(e.name. ljust(35), " | ", e.id.ljust(5) ," | ", e.author.ljust(20)," | " , e.quantity)
        
                
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
        try:
            book.borrow()
            print('Borrow successfully')
            print(book)
        except ValueError as e:
            print(e)
        pass
    def return_book(self):
        pass
    def view_borrowed_book(self):
        pass
        
        



        




library=BookManangement()

library.library = [
    Book("Dế Mèn Phiêu Lưu Ký", "1", "Tô Hoài", 5),
    Book("Tuổi Thơ Dữ Dội", "2", "Phùng Quán", 3),
    Book("Lão Hạc", "3", "Nam Cao", 4),
    Book("Chí Phèo", "4", "Nam Cao", 6),
    Book("Tắt Đèn", "5", "Ngô Tất Tố", 2),
    Book("Vợ Nhặt", "6", "Kim Lân", 3),
    Book("Số Đỏ", "7", "Vũ Trọng Phụng", 5),
    Book("Nhật Ký Trong Tù", "8", "Hồ Chí Minh", 4),
    Book("Rừng Xà Nu", "9", "Nguyễn Trung Thành", 6),
    Book("Đất Rừng Phương Nam", "10", "Đoàn Giỏi", 7),
    Book("Mắt Biếc", "11", "Nguyễn Nhật Ánh", 8),
    Book("Cho Tôi Xin Một Vé Đi Tuổi Thơ", "12", "Nguyễn Nhật Ánh", 6),
    Book("Người Lái Đò Sông Đà", "13", "Nguyễn Tuân", 3),
    Book("Chiếc Thuyền Ngoài Xa", "14", "Nguyễn Minh Châu", 4),
    Book("Vợ Chồng A Phủ", "15", "Tô Hoài", 5),
    Book("Hai Đứa Trẻ", "16", "Thạch Lam", 2),
    Book("Cánh Đồng Bất Tận", "17", "Nguyễn Ngọc Tư", 4),
    Book("Nỗi Buồn Chiến Tranh", "18", "Bảo Ninh", 3),
    Book("Dòng Sông Ly Biệt", "19", "Nguyễn Mộng Giác", 2),
    Book("Bến Không Chồng", "20", "Dương Hướng", 3)
]


library.display_booklist()





library=BookManangement()
library.library=[Book("book1", "ID1", "author1"),Book("book2", "ID2", "author2"),Book("book3", "ID3", "author3")]

library.displayBook()


