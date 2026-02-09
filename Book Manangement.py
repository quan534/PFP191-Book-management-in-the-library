class Book:
    def __init__(self, name, id, author, quantity, category):
        self.name = name
        self.id = id
        self.author = author
        self.quantity = quantity
        self.category=category
 
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
        category = input("Enter Book's category: ")
        book = Book(name, id, author,quantity,category)
        self.library.append(book)
        print("book added!")

 #cho nay neu nhu k co sach thi co display gi ko ong 
# tui sửa rồi nha ô  
   
    def display_booklist(self):
        print("Name".ljust(35), " | ", "Id".ljust(5), " | ", "Author".ljust(20), " | ", "Quantity".ljust(8), " | ", "Category" )
        print("----------------------------------------------------------------------------------------------------------------")
        for e in self.library:
            print(e.name. ljust(35), " | ", e.id.ljust(5) ," | ", e.author.ljust(20)," | " , str(e.quantity).ljust(8), " | ", e.category)
        
                
    def search_for_book(self):
        Name = input('Nhập tên sách: ')
        for n in self.library:
            if n.name == Name:
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
        
def menu():
    print("==========Quản lý thư viện==========")
    print("0. Thoát chương trình")
    print("1. Thêm sách vào thư viện")
    print("2. Hiện thông tin cuốn sách hiện cần")
    print("3. Hiện danh sách các sách thư viện hiện có")
    print("4. Điều chỉnh thông tin sách")
    print("5. Xóa sách")
    print("6. Mượn sách")
    print("7. Trả sách")

library = BookManangement()

while True:
    menu()
    choice = input("Chọn thao tác mà bạn muốn thực hiện")
    if choice == "0":
        break
    elif choice == "1":
        library.addBook()
    elif choice == "2":
        pass
    elif choice == "3":
        pass
    elif choice == "4":
        pass
    elif choice == "5":
        library.delete_book()
    elif choice == "6":
        pass
library=BookManangement()

library.library = [
    Book("Dế Mèn Phiêu Lưu Ký", "1", "Tô Hoài", 5, "Thiếu nhi"),
    Book("Tuổi Thơ Dữ Dội", "2", "Phùng Quán", 3, "Thiếu nhi"),
    Book("Lão Hạc", "3", "Nam Cao", 4, "Văn học Việt Nam"),
    Book("Chí Phèo", "4", "Nam Cao", 6, "Văn học Việt Nam"),
    Book("Tắt Đèn", "5", "Ngô Tất Tố", 2, "Văn học Việt Nam"),
    Book("Vợ Nhặt", "6", "Kim Lân", 3, "Văn học Việt Nam"),
    Book("Số Đỏ", "7", "Vũ Trọng Phụng", 5, "Tiểu thuyết"),
    Book("Nhật Ký Trong Tù", "8", "Hồ Chí Minh", 4, "Thơ"),
    Book("Rừng Xà Nu", "9", "Nguyễn Trung Thành", 6, "Văn học Việt Nam"),
    Book("Đất Rừng Phương Nam", "10", "Đoàn Giỏi", 7, "Thiếu nhi"),
    Book("Mắt Biếc", "11", "Nguyễn Nhật Ánh", 8, "Tiểu thuyết"),
    Book("Cho Tôi Xin Một Vé Đi Tuổi Thơ", "12", "Nguyễn Nhật Ánh", 6, "Thiếu nhi"),
    Book("Người Lái Đò Sông Đà", "13", "Nguyễn Tuân", 3, "Tùy bút"),
    Book("Chiếc Thuyền Ngoài Xa", "14", "Nguyễn Minh Châu", 4, "Truyện ngắn"),
    Book("Vợ Chồng A Phủ", "15", "Tô Hoài", 5, "Văn học Việt Nam"),
    Book("Hai Đứa Trẻ", "16", "Thạch Lam", 2, "Truyện ngắn"),
    Book("Cánh Đồng Bất Tận", "17", "Nguyễn Ngọc Tư", 4, "Truyện ngắn"),
    Book("Nỗi Buồn Chiến Tranh", "18", "Bảo Ninh", 3, "Tiểu thuyết"),
    Book("Dòng Sông Ly Biệt", "19", "Nguyễn Mộng Giác", 2, "Tiểu thuyết"),
    Book("Bến Không Chồng", "20", "Dương Hướng", 3, "Tiểu thuyết")
]


library.display_booklist()

while True:
    print(library.find_book_by_id(input()).__str__())



