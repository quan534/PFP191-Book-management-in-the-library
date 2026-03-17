class Book:
    def __init__(self, name, id, author, quantity, category, borrow_count=0):
        # Khởi tạo thông tin sách
        self.name = name              # Tên sách
        self.id = id                  # ID sách
        self.author = author          # Tác giả
        self.quantity = quantity      # Số lượng còn trong thư viện
        self.category = category      # Thể loại
        self.borrow_count = borrow_count  # Số lượng đang được mượn

    def borrow(self):
        # Hàm mượn sách
        if self.quantity <= 0:
            # Nếu không còn sách thì báo lỗi
            raise ValueError("Sách đã hết, không thể mượn.")
        else: 
            self.quantity -= 1        # Giảm số lượng trong kho
            self.borrow_count += 1    # Tăng số lượng đang mượn

    def return_book(self):
        # Hàm trả sách
        if self.borrow_count <= 0:
            # Không có sách để trả
            raise ValueError("Không có sách nào đang được mượn.")
        self.quantity += 1            # Tăng lại số lượng
        self.borrow_count -= 1        # Giảm số lượng đang mượn
 
    def __str__(self):
        # Hiển thị thông tin sách dạng chuỗi
        return f"Book's name : {self.name}, ID : {self.id}, Author : {self.author}, Quantity : {self.quantity}, Category : {self.category}, Borrowed : {self.borrow_count}"


class BookManangement:
    def __init__(self):
        # Danh sách chứa tất cả sách trong thư viện
        self.library = []
        
    def loadData(file_location):
        # Hàm dự kiến để load dữ liệu (chưa implement)
        pass

    def addBook(self):
        # Nhập thông tin sách từ người dùng
        name = input("Enter Book's name : ")
        id = input("Enter Book's ID : ")
        author = input("Enter Book's Author : ")
        quantityAdd = int(input("Enter the number of books : "))
        category = input("Enter Book's category: ")
        print("Book added!\n")

        # Tạo đối tượng Book mới
        bookadd = Book(name, id, author, quantityAdd, category)

        count = 0
        currCount = 0

        # Đếm số sách hiện có
        for book in self.library:
            currCount += 1

        # Kiểm tra xem sách đã tồn tại chưa
        for book in self.library:
            count += 1
            if book.name == bookadd.name:
                # Nếu trùng tên → cộng thêm số lượng
                book.quantity += quantityAdd
                return
                    
        # Nếu không trùng thì thêm mới
        if count == currCount:
            self.library.append(bookadd)
            self.save_data()


    def importData(self, file_location, method):
        # Mở file để đọc dữ liệu
        file = open(file_location, "r", encoding="utf-8")

        # Nếu chọn overwrite → xóa toàn bộ thư viện hiện tại
        if method == "2":
            self.library = []
            for line in file:   
                # Tách dữ liệu theo dấu phẩy
                name, id, author, quantity, category, borrow = line.strip().split(",")
                book = Book(name, id, author, int(quantity), category, int(borrow))
                self.library.append(book)
            print("Data imported!\n") 
            return
            
        # Nếu append (thêm vào)
        for line in file:   
            print("a") 
            name, id, author, quantity, category, borrow = line.strip().split(",")

            # Kiểm tra trùng ID
            for i, book in enumerate(self.library):
                if book.id == id:
                    # Nếu trùng → cộng dồn số lượng
                    self.library[i] = Book(
                        name, id, author,
                        int(quantity) + book.quantity,
                        category,
                        int(borrow) + book.borrow_count
                    )
                else:
                    # Nếu không trùng → thêm mới
                    book = Book(name, id, author, int(quantity), category, int(borrow))
                    self.library.append(book)

        print("Data imported!\n") 

   
    def display_booklist(self):
        # In tiêu đề bảng
        print("Name".ljust(35), " | ", "Id".ljust(5), " | ", "Author".ljust(20), " | ", "Quantity".ljust(8), " | ", "Category".ljust(20)," | ", "Borrowed".ljust(8))
        print("-------------------------------------------------------------------------------------------------------------------------------")

        # In từng sách
        for e in self.library:
            print(e.name.ljust(35), " | ", e.id.ljust(5) ," | ", e.author.ljust(20)," | " , str(e.quantity).ljust(8), " | ", e.category.ljust(20), " | ", str(e.borrow_count).ljust(8))
        print() 
        

    def search_for_book(self):
        # Tìm sách theo tên
        Name = input('Nhập tên sách: ')
        for n in self.library:
            if n.name == Name:
                print(n.name, " | ID: ", n.id ," | Tác giả: ", n.author,"\n")
                
                
    def edit_book_information(self):
        # Sửa thông tin sách theo ID
        book_id = input("Enter book ID to edit: ")
        book = self.find_book_by_id(book_id)

        if book is None:
            print("Book not found\n")
            return

        print("Leave blank if you don't want to change the information")

        # Nhập thông tin mới
        new_name = input("New name: ")
        new_author = input("New author: ")
        new_quantity = input("New quantity: ")
        new_category = input("New category: ")

        # Chỉ cập nhật nếu có nhập
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
        # Xóa sách theo ID
        removed_ID = input("Enter the removed book's ID : ")
        for book in self.library:
            if book.id == removed_ID:
                self.library.remove(book)
                print("Book removed!\n") 
                return
        print("Book not found\n")


    def find_book_by_id(self, id):
        # Tìm sách theo ID
        for book in self.library:
            if book.id == id:
                return book
        return None
    

    def borrow_book(self, id):
        # Mượn sách theo ID
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


    def return_book(self, id):
        # Trả sách theo ID
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


    def view_borrowed_book(self):
        # Lọc các sách đang được mượn
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
        # Tìm sách theo thể loại
        category = input("Enter category: ").strip()
        found = False

        for book in self.library:
            if book.category.lower() == category.lower():
                print(book)
                found = True

        if not found:
            print("No books found in this category")
    

    def most_borrow_book(self):
        # Tìm sách được mượn nhiều nhất
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
                print("Số sách đã mượn :", book.borrow_count)
                print()


    def save_data(self):
        # Ghi đè file trước
        with open('FileLibrary.txt','w') as f:
            f.close

        # Ghi từng sách vào file
        for info in self.library:
            with open('FileLibrary.txt','a',encoding='UTF-8') as file:
                file.write(f'\n{info.name},{info.id},{info.author},{info.quantity},{info.category}')
