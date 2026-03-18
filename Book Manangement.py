# Lớp Book đại diện cho một cuốn sách trong thư viện
class Book:
    # Hàm khởi tạo các thuộc tính cơ bản của một cuốn sách
    def __init__(self, name, id, author, quantity, category, borrow_count=0):
        self.name = name                 # Tên sách
        self.id = id                     # Mã sách
        self.author = author             # Tác giả
        self.quantity = quantity         # Số lượng sách hiện có trong kho
        self.category = category         # Thể loại sách
        self.borrow_count = borrow_count # Số lượng sách đang được mượn (mặc định là 0)

    # Phương thức xử lý logic khi một cuốn sách được mượn
    def borrow(self):
        # Nếu số lượng trong kho không còn, báo lỗi
        if self.quantity <= 0:
            raise ValueError("Sách đã hết, không thể mượn.")
        else: 
            self.quantity -= 1           # Giảm số lượng trong kho đi 1
            self.borrow_count += 1       # Tăng số lượng đang cho mượn lên 1

    # Phương thức xử lý logic khi một cuốn sách được trả lại
    def return_book(self):
        # Nếu không có ai mượn cuốn này mà lại đem trả thì báo lỗi
        if self.borrow_count <= 0:
            raise ValueError("Không có sách nào đang được mượn.")
        self.quantity += 1               # Tăng số lượng trong kho lên 1
        self.borrow_count -= 1           # Giảm số lượng đang cho mượn đi 1
 
    # Phương thức dunder trả về chuỗi thông tin của sách khi dùng lệnh print()
    def __str__(self):
        return f"Book's name : {self.name}, ID : {self.id}, Author : {self.author}, Quantity : {self.quantity}, Category : {self.category}, Borrowed : {self.borrow_count}"

# Lớp quản lý toàn bộ các cuốn sách trong thư viện
class BookManangement:
    def __init__(self):
        self.library = [] # Khởi tạo danh sách (list) rỗng để chứa các đối tượng Book
        
    def loadData(file_location):
        # Hàm này hiện tại đang để trống (pass), chưa có logic xử lý
        # import data from file_location
        pass

    # Hàm thêm sách mới vào thư viện thông qua nhập liệu từ bàn phím
    def addBook(self):
            name = input("Enter Book's name : ")
            id = input("Enter Book's ID : ")
            author = input("Enter Book's Author : ")
            quantityAdd = int(input("Enter the number of books : "))
            category = input("Enter Book's category: ")
            print("Book added!\n")
            
            # Tạo một đối tượng sách tạm thời từ thông tin vừa nhập
            bookadd = Book(name, id, author,quantityAdd,category)
            count = 0
            currCount = 0
            
            # Đếm tổng số lượng sách hiện có trong thư viện
            for book in self.library:
                currCount += 1
                
            # Duyệt qua từng sách để kiểm tra xem sách mới thêm có bị trùng tên không
            for book in self.library:
                count += 1
                if book.name == bookadd.name:
                    # Nếu trùng tên, chỉ tăng số lượng sách đó lên chứ không tạo sách mới
                    book.quantity += quantityAdd
                    return # Kết thúc hàm luôn
                    
            # Nếu chạy hết vòng lặp mà count bằng currCount (nghĩa là không có sách nào trùng tên)
            if count == currCount:
                self.library.append(bookadd) # Thêm sách mới vào danh sách
                self.save_data()             # Lưu dữ liệu vào file


    # Hàm nhập dữ liệu sách từ file text
    def importData(self, file_location, method):
        file=open(file_location, "r", encoding="utf-8")
        
        # Nếu method == "2" (Ghi đè - Overwrite)
        if method == "2":
            self.library=[] # Làm rỗng danh sách hiện tại
            for line in file:  
                line_data=line.strip().split(",") # Tách các thông tin bằng dấu phẩy
                name, id, author, quantity, category = line_data[:6]
                # Kiểm tra xem dòng dữ liệu có chứa thông tin borrow_count không
                if len(line_data)== 6:
                    borrow=line_data # Chú ý: line_data ở đây là cả một list, logic này có thể gây lỗi kiểu dữ liệu về sau
                else:
                    borrow=0
                # Tạo đối tượng sách và thêm vào danh sách
                book = Book(name, id, author, int(quantity), category, int(borrow))
                self.library.append(book)    
            print("Data imported!\n") 
            return # Đọc xong thì kết thúc hàm
            

        # Phía dưới này là logic cho method "1" (Append - Nối thêm dữ liệu)
        # nếu như có sách trùng thì phải update số lượng sách đó chứ không phải thêm sách mới vào thư viện
        for line in file:   
            line_data=line.strip().split(",")
            name, id, author, quantity, category = line_data[:6]
            if len(line_data)== 6:
                borrow=line_data
            else:
                borrow=0

            # Duyệt danh sách hiện tại để tìm xem có mã sách (id) nào trùng không
            for i, book in enumerate(self.library):
                if book.id == id:
                    # Nếu trùng ID, cộng dồn số lượng và số sách đã mượn
                    self.library[i] = Book(name, id, author, int(quantity)+book.quantity, category, int(borrow)+book.borrow_count)
                else:
                    # Nếu không trùng, tạo sách mới và thêm vào cuối thư viện
                    book = Book(name, id, author, int(quantity), category, int(borrow))
                    self.library.append(book)
        print("Data imported!\n") 
 #cho nay neu nhu k co sach thi co display gi ko ong 
# tui sửa rồi nha ô  
   
    # Hàm hiển thị danh sách toàn bộ sách dưới dạng bảng
    def display_booklist(self):
        # In tiêu đề các cột, dùng .ljust() để căn lề trái tạo thành dạng bảng
        print("Name".ljust(35), " | ", "Id".ljust(5), " | ", "Author".ljust(20), " | ", "Quantity".ljust(8), " | ", "Category".ljust(20)," | ", "Borrowed".ljust(8))
        print("-------------------------------------------------------------------------------------------------------------------------------")
        # In thông tin từng cuốn sách
        for e in self.library:
            print(e.name. ljust(35), " | ", e.id.ljust(5) ," | ", e.author.ljust(20)," | " , str(e.quantity).ljust(8), " | ", e.category.ljust(20), " | ", str(e.borrow_count).ljust(8))
        print() 
        
                
    # Hàm tìm kiếm sách theo tên (Nhập chính xác tên)
    def search_for_book(self):
        Name = input('Nhập tên sách: ')
        for n in self.library:
            if n.name == Name:
                # In ra thông tin sách tìm được (lưu ý: có 2 chữ print lồng nhau ở đây)
                print(print(n.name. ljust(35), " | ", n.id.ljust(5) ," | ", n.author.ljust(20)," | " , str(n.quantity).ljust(8), " | ", n.category.ljust(20), " | ", str(n.borrow_count).ljust(8)))
                
                
    # Hàm chỉnh sửa thông tin sách dựa vào ID
    def edit_book_information(self):
        book_id = input("Enter book ID to edit: ")
        book = self.find_book_by_id(book_id)

        # Nếu không tìm thấy sách thì thông báo và thoát
        if book is None:
            print("Book not found\n")
            return

        print("Leave blank if you don't want to change the information")

        # Cho phép người dùng nhập thông tin mới. Để trống (Enter) nếu không muốn đổi
        new_name = input("New name: ")
        new_author = input("New author: ")
        new_quantity = input("New quantity: ")
        new_category = input("New category: ")

        # Kiểm tra xem người dùng có nhập dữ liệu không, có thì mới cập nhật
        if new_name != "":
            book.name = new_name
        if new_author != "":
            book.author = new_author
        if new_quantity != "":
            book.quantity = int(new_quantity)
        if new_category != "":
            book.category = new_category
            
        self.save_data() # Lưu lại thay đổi vào file
        print("Book information updated successfully!\n")
        print(book)      # In ra thông tin sách sau khi sửa

    # Hàm xóa một cuốn sách dựa trên ID
    def delete_book(self):
        removed_ID = input("Enter the removed book's ID : ")
        for book in self.library:
            if book.id == removed_ID:
                self.library.remove(book) # Xóa đối tượng sách khỏi danh sách
                print("Book removed!\n") 
                self.save_data()          # Cập nhật lại file lưu trữ
                return
        # Báo lỗi nếu chạy hết vòng for mà không thấy ID tương ứng
        print("Book not found\n")

    # Hàm hỗ trợ: Tìm và trả về đối tượng sách nếu ID khớp, nếu không trả về None
    def find_book_by_id(self, id):
        for book in self.library:
            if book.id == id:
                return book
        return None
    
    # Hàm thực hiện thao tác mượn sách
    def borrow_book(self,id):
        book = self.find_book_by_id(id)
        if book is None:
            print('Book not found\n')
            return
        # Sử dụng khối try-except để bắt lỗi ValueError (ví dụ: kho hết sách) từ hàm borrow() của class Book
        try:
            book.borrow() # Gọi phương thức mượn của class Book
            print('Borrow successfully')
            print(book)
            print() 
        except ValueError as e:
            print(e)
            print() 
        self.save_data() # Lưu thay đổi trạng thái số lượng
        pass

    # Hàm thực hiện thao tác trả sách
    def return_book(self,id):
        book = self.find_book_by_id(id)
        if book is None:
            print('Book not found\n')
            return
        # Sử dụng try-except để bắt lỗi (ví dụ: chưa ai mượn mà đi trả)
        try:
            book.return_book() # Gọi phương thức trả của class Book
            print('Return successfully')
            print(book)
            print() 
        except ValueError as e:
            print(e)
            print()
        self.save_data()
        pass

    # Hàm liệt kê các sách đang có người mượn
    def view_borrowed_book(self):
        """Hiển thị các sách đang có người mượn (borrow_count > 0)"""
        # Dùng List Comprehension để lọc ra các sách có borrow_count > 0
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

    # Hàm liệt kê sách theo thể loại (Category)
    def books_by_category(self):
        category = input("Enter category: ").strip()

        found = False

        for book in self.library:
            # So sánh không phân biệt chữ hoa chữ thường
            if book.category.lower() == category.lower():
                print(book)
                found = True

        if not found:
            print("No books found in this category")
    
    # Hàm tìm cuốn sách được mượn nhiều nhất
    def most_borrow_book(self):
        list_borrow_count = []
        # Lấy ra danh sách toàn bộ lượt mượn của các sách
        for book in self.library:
            list_borrow_count.append(book.borrow_count)
            
        max_borrow_count = max(list_borrow_count) # Tìm số lượt mượn lớn nhất
        
        if max_borrow_count == 0:
            print("Khong co quyen sach nao duoc muon")
            print()
            return

        print("Cac quyen sach duoc muon nhieu nhat la")
        print() 
        # In ra thông tin của tất cả các cuốn sách có lượt mượn bằng với số lớn nhất vừa tìm được
        for book in self.library:
            if book.borrow_count == max_borrow_count:
                print(book.name)
                print("Số sách đã mượn :",book.borrow_count)
                print()
                
    # Hàm lưu dữ liệu hiện tại của thư viện vào file text
    def save_data(self):
        # Mở file chế độ 'w' (write) để xóa trắng nội dung cũ (Lưu ý: lệnh f.close đang thiếu dấu ngoặc tròn ())
        with open('FileLibrary.txt','w') as f:
            f.close
            
        # Mở file chế độ 'a' (append) để ghi nối tiếp từng dòng dữ liệu sách vào
        for info in self.library:
            with open('FileLibrary.txt','a',encoding='UTF-8') as file:
                file.write(f'{info.name},{info.id},{info.author},{info.quantity},{info.category}\n')
        
# Hàm hiển thị giao diện menu điều khiển ra màn hình
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
    print("9. Xem danh sách mượn")
    print("10. Tìm sách được mượn nhiều nhất")
    print() 

# --- PHẦN CHẠY CHÍNH CỦA CHƯƠNG TRÌNH ---

# Khởi tạo đối tượng quản lý thư viện
library = BookManangement()

# Khởi tạo và load dữ liệu mẫu từ file ban đầu (method "2" = ghi đè)
library.importData("FileLibrary.txt","2")

# Vòng lặp vô hạn để giữ cho menu luôn hiện ra sau khi thực hiện xong 1 chức năng
while True:
    menu()
    choice = input("Chọn thao tác mà bạn muốn thực hiện: ")
    print() 
    
    # Kiểm tra lựa chọn và gọi các hàm tương ứng từ class BookManagement
    if choice == "0":
        break # Thoát khỏi vòng lặp vô hạn, kết thúc chương trình
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
        library.view_borrowed_book()
    elif choice == "10":
        library.most_borrow_book()