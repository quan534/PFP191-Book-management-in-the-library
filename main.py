def edit_book (self, book_id, **kwargs):
    try:
        book = self.books[book_id]
    except KeyErrol:
        raise KeyErrol("Book not found")
    
    for k, v in kwargs.items():
    v is not None and setattr(book, f"_{k}", v)

     
