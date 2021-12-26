from book import *
from constant import *
from tools import *


# Generic tree node class
class TreeNode(object):
    def __init__(self, val: str, book_info: Book):
        self.val = val
        self.book_info = book_info
        self.left = None
        self.right = None
        self.height = 1


class AVLTree(object):
    """
    Adapt from https://alphafan.github.io/posts/avl_tree.html
    """
    # Recursive function to insert key in
    # subtree rooted with node and returns
    # new root of subtree.
    def insert(self, root, title, book_info):
        # Step 1 - Perform normal BST
        if not root:
            return TreeNode(title, book_info)
        elif title < root.val:
            root.left = self.insert(root.left, title, book_info)
        elif title > root.val:
            root.right = self.insert(root.right, title, book_info)
        elif title == root.val:
            root.book_info.book_id.append(book_info.book_id[0])
            root.book_info.is_available.append(book_info.is_available[0])

        # Step 2 - Update the height of the
        # ancestor node
        root.height = 1 + max(self.get_height(root.left),
                              self.get_height(root.right))

        # Step 3 - Get the balance factor
        balance = self.get_balance(root)

        # Step 4 - If the node is unbalanced,
        # then try out the 4 cases
        # Case 1 - Left Left
        if balance > 1 and title < root.left.val:
            return self.right_rotate(root)

        # Case 2 - Right Right
        if balance < -1 and title > root.right.val:
            return self.left_rotate(root)

        # Case 3 - Left Right
        if balance > 1 and title > root.left.val:
            root.left = self.left_rotate(root.left)
            return self.right_rotate(root)

        # Case 4 - Right Left
        if balance < -1 and title < root.right.val:
            root.right = self.right_rotate(root.right)
            return self.left_rotate(root)

        return root

    def left_rotate(self, z):
        y = z.right
        T2 = y.left

        # Perform rotation
        y.left = z
        z.right = T2

        # Update heights
        z.height = 1 + max(self.get_height(z.left),
                           self.get_height(z.right))
        y.height = 1 + max(self.get_height(y.left),
                           self.get_height(y.right))

        # Return the new root
        return y

    def right_rotate(self, z):
        y = z.left
        T3 = y.right

        # Perform rotation
        y.right = z
        z.left = T3

        # Update heights
        z.height = 1 + max(self.get_height(z.left),
                           self.get_height(z.right))
        y.height = 1 + max(self.get_height(y.left),
                           self.get_height(y.right))

        # Return the new root
        return y

    def get_height(self, root):
        if not root:
            return 0

        return root.height

    def get_balance(self, root):
        if not root:
            return 0

        return self.get_height(root.left) - self.get_height(root.right)

    def pre_order(self, root):
        if not root:
            return
        print_func(root.book_info)

        self.pre_order(root.left)
        self.pre_order(root.right)

    def borrow_book(self, root, title):
        borrow_book = None
        if not root:
            return None
        elif title < root.val:
            self.borrow_book(root.left, title)
        elif title > root.val:
            self.borrow_book(root.right, title)
        else:
            if '1' in root.book_info.is_available:
                for i in range(len(root.book_info.book_id)):
                    if root.book_info.is_available[i] == '1':
                        borrow_book = Book(root.book_info.title, root.book_info.category, root.book_info.genre,
                                           root.book_info.book_id[i], root.book_info.is_available[i])
                        root.book_info.is_available[i] = '0'
                        break

        return borrow_book

    def return_book(self, root, title, book_id):
        return_book = None
        if not root:
            return None
        elif title < root.val:
            self.return_book(root.left, title, book_id)
        elif title > root.val:
            self.return_book(root.right, title, book_id)
        else:
            for i in range(len(root.book_info.book_id)):
                if root.book_info.book_id[i] == book_id:
                    root.book_info.is_available[i] = '1'
                    return_book = 1
                    break

        return return_book

    def get_book(self, root, title):
        get_book = None
        if not root:
            return None
        elif title < root.val:
            self.get_book(root.left, title)
        elif title > root.val:
            self.get_book(root.right, title)
        else:
            get_book = root.book_info

        return get_book
