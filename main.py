from os import system
from book import Book
from library import Library
import sys
#sys.stdout.reconfigure(encoding='ansi')    # раскомментировать если не отображается кириллица

system('cls')

library = Library()

def main_menu():
    while True:
        answer = input("\tMENU:\n"
                       "1 - SHOW ALL | "
                       "2 - ADD | "
                       "3 - SEARCH | "
                       "4 - СHANGE STATUS | "
                       "5 - DELETE | "
                       "6 - EXIT\n"
                       ">> ")

        if answer == "1":
            print("All books:")
            if len(library.show_all_books()) > 0:
                for book in library.show_all_books():
                    print(book)
            else:
                print("No books in the library!")

        elif answer == "2":
            print('Adding a new book:')
            title = input("Title: ").strip()
            author = input("Author: ").strip()
            year = input("Year: ").strip()
            library.add_book(title, author, year)
            print("New Book added!")

        elif answer == "3":
            print("Search book by: ", "1-Title ", "2-Author ", "3-Year")
            answer = input(">>> ").strip()
            result = []
            if answer == '1':
                title_book = input("Enter book title: ").strip()
                result = library.search_books('title', title_book)
            elif answer == '2':
                author_book = input("Enter book author: ").strip()
                result = library.search_books('author', author_book)
            elif answer == '3':
                year_book = input("Enter book year: ").strip()
                result = library.search_books('year', year_book)
            print_result_search_books(result)

        elif answer == "4":
            process_book_action("Status change", library.change_status_book)

        elif answer == "5":
            process_book_action("Delete", library.delete_book)

        elif answer == "6":
            print("Bye!")
            break
        else:
            print("Try again!\n")
        print()


def print_result_search_books(result: list[Book]) -> None:
    """Prints result of search_books function

    Args:
        result (list[Book]): list of objects books

    Returns:
        None
    """
    if result:
        for book in result:
            print(book)
    else:
        print("Book not found!")


def process_book_action(action_name: str, action_function: callable) -> None:
    """
    Process book action - change status or delete of book

    :param action_name: (str) Name of action. For example: "Status change", "Delete"
    :param action_function: (callable) Action function. May be change_status_book() or delete_book() methods of Library class

    :return: None
    """
    print(f"{action_name}:")
    id_book = input("Enter book ID: ").strip()
    target_book = library.search_book_by_id(id_book)

    if target_book:
        print(target_book)
        confirmation = input(f"Do you want to {action_name.lower()} this book? (y/n): ").strip().lower()

        if confirmation == 'y':
            action_function(target_book)
            print(f"Book {action_name.lower()}d!")
    else:
        print("Book not found!")


if __name__ == '__main__':
    main_menu()
