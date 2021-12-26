class Book:
    def __init__(self, title: str, category: str, genre: str, book_id: str, is_available: str):
        self.title = title
        self.category = category
        self.genre = genre

        self.book_id = []
        self.is_available = []
        self.book_id.append(book_id)
        self.is_available.append(is_available)

        assert len(self.book_id) == len(self.is_available), 'Book number does not match!'
