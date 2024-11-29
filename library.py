from os import path
from book import Book
from datetime import datetime


class Library:
    """
    The public class representing the book library.

        Attributes:
            books: (list[Book]) List of objects Book
            file_db: (str) Path to the database file
            max_id: (int) Max id of the books

        Methods:
            show_all_books(): lists all books
            add_book(title: str, author: str, year: str): adds a book to the library
            search_book_by_id(id_book: str): searches a book by id in the library
            search_books(criteria: str, value: str): search for books by title, author, or year of publication
            change_status_book(changed_book: Book): changes the status of a book
            delete_book(deleting_book: Book): deletes a book from the library
            __save_to_file(): saves library data to a file (if the file does not exist, it is created)
            __validate_entered_id(id_book: str): validates the entered id
            __validate_entered_year(year: str): validates the entered year
            __validate_entered_author(author: str): validates the entered author
    """
    def __init__(self, file_db: str="books_db.txt"):
        """"
        Constructor of the Library class.

        Args:
            file_db: (str) Path to the database file. If the file does not exist, it is created.
                If the file exists, it is read and the data is loaded into the list.

        Returns:
            None

        Raises:
            None

        Attributes:
            books: (list[Book]) List of objects Book
            file_db: (str) Path to the database file
            max_id: (int) Max id of the books
        """
        self.books: list[Book] = []
        self.file_db: str = file_db
        self.max_id: int = 0

        if not path.exists(self.file_db):
            with open(self.file_db, "w", encoding="utf-8") as _:
                pass
        else:
            with open(self.file_db, "r", encoding="utf-8") as f:
                if path.getsize(self.file_db) > 0:
                    for line in f:
                        if not line.strip() or line.strip() == '\n':
                            continue
                        try:
                            book = Book(*line.strip().split(";"))
                        except TypeError:
                            print("File data base is incorrect!")
                            exit()
                        self.books.append(book)
                    self.max_id = int(self.books[-1].id)

    def show_all_books(self) -> list[Book]:
        """
        Lists all books in the library.

        :return: (list[Book]) List
        """
        return self.books

    def add_book(self, title: str, author: str, year: str) -> None:
        """
        Adds a book to the library.

        :return: None

        :param title: (str) Title of the book
        :param author: (str) Author of the book
        :param year: (str) Year of publication of the book
        """
        if title != '' and self.__validate_entered_author(author) > 0 and self.__validate_entered_year(year) > 0:
            self.max_id += 1
            new_book = Book(self.max_id, title, author, int(year))
            self.books.append(new_book)
            with open(self.file_db, "a", encoding="utf-8") as f:
                f.write(f"{self.max_id};{new_book.title};{new_book.author};{new_book.year};{new_book.status}\n".replace('\r\n', '\n'))

    def search_book_by_id(self, id_book: str) -> Book | None:
        """"
        Searches a book by id in the library.

        :return: (Book) Book object or None

        :param id_book: (str) ID of the book
        """
        if self.__validate_entered_id(id_book) > 0:
            for book in self.books:
                if int(book.id) == int(id_book):
                    return book
            return None

    def search_books(self, criteria: str, value: str) -> list[Book]:
        """"
        Search for books by title, author, or year of publication.

        :return: (list[Book]) List of objects books

        :param criteria: (str) Criteria for searching. May be 'title', 'author', or 'year'
        :param value: (str) Value for searching
        """
        result = []
        if criteria == 'title':
            if value != '':
                for book in self.books:
                    if book.title.strip().lower() == value.lower():
                        result.append(book)
        elif criteria == 'author':
            if self.__validate_entered_author(value) > 0:
                for book in self.books:
                    if book.author.strip().lower() == value.lower():
                        result.append(book)
        elif criteria == 'year':
            if self.__validate_entered_year(value) > 0:
                for book in self.books:
                    if int(book.year) == int(value):
                        result.append(book)
        return result

    def change_status_book(self, changed_book: Book) -> None:
        """"
        Changes the status of the book.

        :return: None

        :param changed_book: (Book) Book object
        """
        changed_book.switch_status_book()
        self.__save_to_file()

    def delete_book(self, deleting_book: Book) -> None:
        """"
        Deletes a book from the library.

        :return: None

        :param deleting_book: (Book) Book object
        """
        self.books.remove(deleting_book)
        self.__save_to_file()

    def __save_to_file(self) -> None:
        """"
        Saves the data (books) to the file.

        :return: None
        """
        with open(self.file_db, "w", encoding="utf-8", newline="") as f:
            for book in self.books:
                if book == '\n' or book == '\n\n' or book == '\r' or book == '' or book is None:
                     continue
                if book.id == '' and book.title == '' and book.author == '' and book.status == '':
                    continue
                f.write(f"{book.id};{book.title};{book.author};{book.year};{book.status}\n".replace('\r\n', '\n'))

    def __validate_entered_id(self, id_book: str) -> int:
        """"
        Validates the entered ID.

        :return: (int) 1 - if the ID is valid, -1 - if the ID is not entered, -2 - if the ID is invalid

        :param id_book: (str) ID of the book
        """
        if not id_book:
            print("ID don't entered for search")
            return -1
        if not id_book.isdigit() or int(id_book) < 1 or int(id_book) > self.max_id:
            print("invalid ID entered!")
            return -2
        return 1

    def __validate_entered_year(self, year: str) -> int:
        """"
        Validates the entered year.

        :return: (int) 1 - if the year is valid, -1 - if the year is not entered, -2 - if the year is invalid

        :param year: (str) Year of publication of the book
        """
        if not year:
            print("Year don't entered for search")
            return -1
        if not year.isdigit() or int(year) < 1457 or int(
                year) > datetime.now().year:  # первые печатные книги появились в 1457 году
            print("invalid Year entered!")
            return -2
        return 1

    def __validate_entered_author(self, name: str) -> int:
        """"
        Validates the entered author.

        :return: (int) 1 - if the author is valid, -1 - if the author is not entered, -2 - if the author is invalid

        :param name: (str) Author of the book
        """
        if not name:
            print("Author don't entered for search")
            return -1
        parts = name.split('.') if '.' in name else [name]
        for part in parts:
            if "-" in part:
                part = part.replace("-", "")
            if not part.strip().isalpha():
                print("Invalid author entered!")
                return -2
        return 1
