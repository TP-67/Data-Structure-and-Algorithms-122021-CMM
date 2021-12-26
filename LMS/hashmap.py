from avl import *
from constant import *
from tools import *


class HashMap:
    """
    Adapt from https://www.tutorialspoint.com/design-hashmap-in-python
    """
    def __init__(self):
        self.size = 1033
        self.data = [AVLTree() for _ in range(self.size)]
        self.root = [None for _ in range(self.size)]

    def _hash(self, key):
        return hash_func(key, self.size)

    def put_book_in_tree(self, genre, book_info) -> str:
        h = self._hash(genre)
        self.root[h] = self.data[h].insert(self.root[h], book_info.title, book_info)

        return 'Insert book success!'

    def get_genre_from_tree(self, genre):
        h = self._hash(genre)
        self.data[h].pre_order(self.root[h])

    def borrow_book_from_tree(self, title) -> str:
        result = None
        for i in range(len(GENRE_LIST)):
            h = self._hash(GENRE_LIST[i])
            result = self.data[h].borrow_book(self.root[h], title)
            if result is not None:
                break

        if result is None:
            return 'Record not found!'
        else:
            return 'Borrow book success!'

    def return_book_to_tree(self, title, book_id) -> str:
        result = None
        for i in range(len(GENRE_LIST)):
            h = self._hash(GENRE_LIST[i])
            result = self.data[h].return_book(self.root[h], title, book_id)
            if result is not None:
                break

        if result is None:
            return 'Record not found!'
        else:
            return 'Return book success!'

    def get_book_from_tree(self, title):
        result = None
        for i in GENRE_LIST:
            h = self._hash(i)
            result = self.data[h].get_book(self.root[h], title)
            if result is not None:
                break

        print_func(result)
