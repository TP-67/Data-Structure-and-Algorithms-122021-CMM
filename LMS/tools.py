import os
import sys
import termios
from book import *


def press_any_key_exit(msg):
    """
    Adapt from https://www.jb51.net/article/93504.htm
    :param msg:
    :return:
    """
    fd = sys.stdin.fileno()

    old_tty_info = termios.tcgetattr(fd)

    new_tty_info = old_tty_info[:]

    new_tty_info[3] &= ~termios.ICANON
    new_tty_info[3] &= ~termios.ECHO

    sys.stdout.write(msg)
    sys.stdout.flush()
    termios.tcsetattr(fd, termios.TCSANOW, new_tty_info)
    os.read(fd, 7)

    termios.tcsetattr(fd, termios.TCSANOW, old_tty_info)


def hash_func(key: str, size: int) -> int:
    asc_key = 0
    for i in key:
        if i.isupper():
            asc_key += ord(i) - 65 + 1
        elif i.islower():
            asc_key += ord(i) - 97 + 1
        else:
            asc_key += 0

    return asc_key % size


def print_func(book: Book):
    if book is None:
        print('No book record!')
    else:
        print('We have {0} copy of this book available :)'.format(book.is_available.count('1')))
        for i in range(len(book.book_id)):
            if book.is_available[i] == '0':
                availability = 'On-loan'
            else:
                availability = 'Available'

            print('==> Title: ' + book.title + ', Category: ' + book.category + ', Genre: ',
                  book.genre + ', Book Id: ', book.book_id[i] + ', Availability: ' + availability)
