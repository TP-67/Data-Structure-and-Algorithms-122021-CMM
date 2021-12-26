import os
from hashmap import *
from constant import *
from tools import *


def build_lib():
    apu_lib = HashMap()
    for i in range(len(BOOKS)):
        apu_lib.put_book_in_tree(BOOKS[i][2], Book(BOOKS[i][0], BOOKS[i][1], BOOKS[i][2], BOOKS[i][3], BOOKS[i][4]))
    return apu_lib


def welcome_msg(apu_lib: HashMap):

    os.system('clear')
    print()
    print('**************************************************')
    print('*                                                *')
    print('*                                                *')
    print('*        Welcome to APU Library                  *')
    print('*        1) Borrow books                         *')
    print('*        2) Return books                         *')
    print('*        3) Look for books                       *')
    print('*        4) Display books of a specific genre     *')
    print('*        5) Insert a new copy of books           *')
    print('*        6) Exit                                 *')
    print('*                                                *')
    print('**************************************************')
    print()

    choice = input('Please input your choice: ')

    if choice == '1':

        os.system('clear')
        print()
        print('**************************************************')
        print('*                                                *')
        print('*                                                *')
        print('*                                                *')
        print('*                                                *')
        print('*        Please input book title:                *')
        print('*                                                *')
        print('*                                                *')
        print('*                                                *')
        print('*                                                *')
        print('*                                                *')
        print('**************************************************')
        print()

        title = input()
        result = apu_lib.borrow_book_from_tree(title)
        print(result)

        press_any_key_exit('Press any key  to continue...')
        os.system('clear')

    elif choice == '2':

        os.system('clear')
        print()
        print('**************************************************')
        print('*                                                *')
        print('*                                                *')
        print('*                                                *')
        print('*                                                *')
        print('*        Please input book title & book Id:      *')
        print('*                                                *')
        print('*                                                *')
        print('*                                                *')
        print('*                                                *')
        print('*                                                *')
        print('**************************************************')
        print()

        title, book_id = input().split(',')
        title = title.strip()
        book_id = book_id.strip()
        result = apu_lib.return_book_to_tree(title, book_id)
        print(result)

        press_any_key_exit('Press any key  to continue...')
        os.system('clear')

    elif choice == '3':

        os.system('clear')
        print()
        print('**************************************************')
        print('*                                                *')
        print('*                                                *')
        print('*                                                *')
        print('*                                                *')
        print('*        Please input book title:                *')
        print('*                                                *')
        print('*                                                *')
        print('*                                                *')
        print('*                                                *')
        print('*                                                *')
        print('**************************************************')
        print()

        title = input()
        result = apu_lib.get_book_from_tree(title)

        press_any_key_exit('Press any key  to continue...')
        os.system('clear')

    elif choice == '4':

        os.system('clear')
        print()
        print('**************************************************')
        print('*                                                *')
        print('*                                                *')
        print('*                                                *')
        print('*                                                *')
        print('*        Please input genre:                     *')
        print('*                                                *')
        print('*                                                *')
        print('*                                                *')
        print('*                                                *')
        print('*                                                *')
        print('**************************************************')
        print()

        genre = input()
        if genre not in GENRE_LIST:
            print('Record not found!')
        else:
            result = apu_lib.get_genre_from_tree(genre)

        press_any_key_exit('Press any key  to continue...')
        os.system('clear')

    elif choice == '5':

        os.system('clear')
        print()
        print('**************************************************')
        print('*                                                *')
        print('*                                                *')
        print('*                                                *')
        print('*                                                *')
        print('*        Please input book genre & book info:    *')
        print('*                                                *')
        print('*                                                *')
        print('*                                                *')
        print('*                                                *')
        print('*                                                *')
        print('**************************************************')
        print()

        title, category, genre, book_id, availability = input().split(',')
        title = title.strip()
        category = category.strip()
        genre = genre.strip()
        book_id = book_id.strip()
        availability = availability.strip()

        if genre not in GENRE_LIST or category not in CATEGORY_LIST:
            print('Record not found!')
        else:
            result = apu_lib.put_book_in_tree(genre, Book(title, category, genre, book_id, availability))
            print(result)

        press_any_key_exit('Press any key  to continue...')
        os.system('clear')

    elif choice == '6':

        os.system('clear')
        print()
        print('**************************************************')
        print('*                                                *')
        print('*                                                *')
        print('*                                                *')
        print('*                                                *')
        print('*                  Good Bye !                    *')
        print('*                                                *')
        print('*                                                *')
        print('*                                                *')
        print('*                                                *')
        print('*                                                *')
        print('**************************************************')
        print()

    else:
        pass

    return choice


if __name__ == '__main__':

    apu_lib = build_lib()

    choice = '0'
    while choice != '6':
        choice = welcome_msg(apu_lib)
