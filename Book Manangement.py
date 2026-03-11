class Book:
    def __init__(self, name, id, author, quantity, category, borrow_count=0):
        self.name = name
        self.id = id
        self.author = author
        self.quantity = quantity
        self.category=category
        self.borrow_count = borrow_count
    def borrow(self):
        if self.quantity <= 0:
            raise ValueError("Sách đã hết, không thể mượn.")
        else: 
            self.quantity -= 1
            self.borrow_count += 1

    def return_book(self):
        if self.borrow_count <= 0:
            raise ValueError("Không có sách nào đang được mượn.")
        self.quantity += 1
        self.borrow_count -= 1
 
    def __str__(self):
        return f"Book's name : {self.name}, ID : {self.id}, Author : {self.author}, Quantity : {self.quantity}, Category : {self.category}, Borrowed : {self.borrow_count}"

class BookManangement:
    def __init__(self):
        self.library = []
        
    def loadData(file_location):
        # import data from file_location
        pass

    def addBook(self):
            name = input("Enter Book's name : ")
            id = input("Enter Book's ID : ")
            author = input("Enter Book's Author : ")
            quantityAdd = int(input("Enter the number of books : "))
            category = input("Enter Book's category: ")
            print("Book added!\n")
            bookadd = Book(name, id, author,quantityAdd,category)
            count = 0
            currCount = 0
            for book in self.library:
                currCount += 1
            for book in self.library:
                count += 1
                if book.name == bookadd.name:
                    book.quantity += quantityAdd
                    return
                    
            if count == currCount:
                self.library.append(bookadd)
                save_data(bookadd)


    def importData(self, file_location, method):
        file=open(file_location, "r", encoding="utf-8")
        if method == "2":
            self.library=[]
            for line in file:   
                name, id, author, quantity, category, borrow = line.strip().split(",")
                book = Book(name, id, author, int(quantity), category, int(borrow))
                self.library.append(book)    
            print("Data imported!\n") 
            return
            

        # nếu như có sách trùng thì phải update số lượng sách đó chứ không phải thêm sách mới vào thư viện
        for line in file:   
            print("a") 
            name, id, author, quantity, category, borrow = line.strip().split(",")
            for i, book in enumerate(self.library):
                if book.id == id:
                    self.library[i] = Book(name, id, author, int(quantity)+book.quantity, category, int(borrow)+book.borrow_count)
                else:
                    book = Book(name, id, author, int(quantity), category, int(borrow))
                    self.library.append(book)
        print("Data imported!\n") 
 #cho nay neu nhu k co sach thi co display gi ko ong 
# tui sửa rồi nha ô  
   
    def display_booklist(self):
        print("Name".ljust(35), " | ", "Id".ljust(5), " | ", "Author".ljust(20), " | ", "Quantity".ljust(8), " | ", "Category".ljust(20)," | ", "Borrowed".ljust(8))
        print("-------------------------------------------------------------------------------------------------------------------------------")
        for e in self.library:
            print(e.name. ljust(35), " | ", e.id.ljust(5) ," | ", e.author.ljust(20)," | " , str(e.quantity).ljust(8), " | ", e.category.ljust(20), " | ", str(e.borrow_count).ljust(8))
        print() 
        
                
    def search_for_book(self):
        Name = input('Nhập tên sách: ')
        for n in self.library:
            if n.name == Name:
                print(n.name, " | ID: ", n.id ," | Tác giả: ", n.author,"\n")
                
                
    def edit_book_information(self):
        book_id = input("Enter book ID to edit: ")
        book = self.find_book_by_id(book_id)

        if book is None:
            print("Book not found\n")
            return

        print("Leave blank if you don't want to change the information")

        new_name = input("New name: ")
        new_author = input("New author: ")
        new_quantity = input("New quantity: ")
        new_category = input("New category: ")

        if new_name != "":
            book.name = new_name
        if new_author != "":
            book.author = new_author
        if new_quantity != "":
            book.quantity = int(new_quantity)
        if new_category != "":
            book.category = new_category

        print("Book information updated successfully!\n")
        print(book)



        
    def delete_book(self):
        removed_ID = input("Enter the removed book's ID : ")
        for book in self.library:
            if book.id == removed_ID:
                self.library.remove(book)
                print("Book removed!\n") 
                return
        print("Book not found\n")

    def find_book_by_id(self, id):
        for book in self.library:
            if book.id == id:
                return book
        return None
    
    def borrow_book(self,id):
        book = self.find_book_by_id(id)
        if book is None:
            print('Book not found\n')
            return
        try:
            book.borrow()
            print('Borrow successfully')
            print(book)
            print() 
        except ValueError as e:
            print(e)
            print() 
        pass

    def return_book(self,id):
        book = self.find_book_by_id(id)
        if book is None:
            print('Book not found\n')
            return
        try:
            book.return_book()
            print('Return successfully')
            print(book)
            print() 
        except ValueError as e:
            print(e)
            print() 
        pass

    def view_borrowed_book(self):
        """Hiển thị các sách đang có người mượn (borrow_count > 0)"""
        borrowed = [book for book in self.library if book.borrow_count > 0]
        if not borrowed:
            print("Hiện không có cuốn sách nào đang được mượn.")
            return

        print("\n=== DANH SÁCH SÁCH ĐANG ĐƯỢC MƯỢN ===")
        print("Tên sách".ljust(35), " | ", "ID".ljust(5), " | ", "Tác giả".ljust(20), " | ", "Số lượng đang mượn")
        print("-" * 85)
        for book in borrowed:
            print(book.name.ljust(35), " | ", book.id.ljust(5), " | ", book.author.ljust(20), " | ", str(book.borrow_count))
        print()

    def books_by_category(self):
        category = input("Enter category: ").strip()

        found = False

        for book in self.library:
            if book.category.lower() == category.lower():
                print(book)
                found = True

        if not found:
            print("No books found in this category")
    
    def most_borrow_book(self):
        list_borrow_count = []
        for book in self.library:
            list_borrow_count.append(book.borrow_count)
        max_borrow_count = max(list_borrow_count)
        if max_borrow_count == 0:
            print("Khong co quyen sach nao duoc muon")
            print()
            return

        print("Cac quyen sach duoc muon nhieu nhat la")
        print() 
        for book in self.library:
            if book.borrow_count == max_borrow_count:
                print(book.name)
                print("Số sách đã mượn :",book.borrow_count)
                print()
def save_data(info):
    with open('FileLibrary.txt','a',encoding='UTF-8') as file:
        file.write(f'\n{info.name},{info.id},{info.author},{info.quantity},{info.category}')
        
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
    print("8. Nhập dữ liệu từ file")
    print("9. Lưu dữ liệu ra file")
    print("10. Tìm sách được mượn nhiều nhất")
    print() 

library = BookManangement()

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

while True:
    menu()
    choice = input("Chọn thao tác mà bạn muốn thực hiện: ")
    print() 
    if choice == "0":
        break
    elif choice == "1":
        library.addBook()
    elif choice == "2":
        library.search_for_book()
    elif choice == "3":
        library.display_booklist()
    elif choice == "4":
        library.edit_book_information()
    elif choice == "5":
        library.delete_book()
    elif choice == "6":
        id = input('Nhập ID sách bạn muốn mượn: ')
        library.borrow_book(id)
    elif choice == "7":
        id = input('Nhập ID sách bạn muốn trả: ')
        library.return_book(id)
    elif choice == "8":
        filename = input("Nhập tên file dữ liệu: ")
        method = input("Type: 1.Append 2.Overwrite : ")
        library.importData(filename, method)
    elif choice == "9":
        pass
    elif choice == "10":
        library.most_borrow_book()















