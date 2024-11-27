import os
import unittest
from library import Library
from book import Book

class TestAddBook(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        """Определяет временный файл перед запуском тестов"""
        cls.test_file = 'tmp_db.txt'

    @classmethod
    def tearDownClass(cls):
        """Удаляет временный файл после завершения тестов"""
        if os.path.exists(cls.test_file):
            os.remove(cls.test_file)

    def setUp(self):
        """Создает временный файл перед запуском тестов"""
        self.library = Library(file_db="tmp_db.txt")

    def tearDown(self):
        """Очищает тестовые данные после каждого теста"""
        self.library.books = []
        with open(self.library.file_db, "w", encoding="utf-8") as _:
            pass


    def test_add_book_to_empty_library(self):
        """Добавляет книгу в пустую библиотеку"""
        self.library.add_book('Война и мир', 'Л.Н. Толстой', '1868')
        self.assertEqual(self.library.books[0].id, 1)
        self.assertEqual(self.library.books[0].title, 'Война и мир')
        self.assertEqual(self.library.books[0].author, 'Л.Н. Толстой')
        self.assertEqual(self.library.books[0].year, 1868)
        self.assertEqual(self.library.books[0].status, 1)

    def test_add_book_to_empty_file(self):
        """Добавляет книгу в пустой файл"""
        self.library.add_book('Морской волк', 'Дж. Лондон', '1904')
        with open(self.library.file_db, "r", encoding="utf-8") as f:
            for line in f:
                book = Book(*line.strip().split(";"))
                self.library.books.append(book)
        self.assertEqual(self.library.books[0].id, 1)
        self.assertEqual(self.library.books[0].title, 'Морской волк')
        self.assertEqual(self.library.books[0].author, 'Дж. Лондон')
        self.assertEqual(self.library.books[0].year, 1904)
        self.assertEqual(self.library.books[0].status, 1)

    def test_add_book_to_not_empty_library(self):
        """Добавляет книгу в непустую библиотеку"""
        self.library.add_book('Морской волк', 'Дж. Лондон', '1904')
        self.library.add_book('Война и мир', 'Л.Н. Толстой', '1868')
        self.assertEqual(self.library.books[-1].id, 2)
        self.assertEqual(self.library.books[-1].title, 'Война и мир')
        self.assertEqual(self.library.books[-1].author, 'Л.Н. Толстой')
        self.assertEqual(self.library.books[-1].year, 1868)
        self.assertEqual(self.library.books[-1].status, 1)

    def test_add_book_to_not_empty_file(self):
        """Добавляет книгу в непустой файл"""
        self.library.add_book('Морской волк', 'Дж. Лондон', '1904')
        self.library.add_book('Война и мир', 'Л.Н. Толстой', '1868')
        with open(self.library.file_db, "r", encoding="utf-8") as f:
            for line in f:
                book = Book(*line.strip().split(";"))
                self.library.books.append(book)
        self.assertEqual(self.library.books[-1].id, '2')
        self.assertEqual(self.library.books[-1].title, 'Война и мир')
        self.assertEqual(self.library.books[-1].author, 'Л.Н. Толстой')
        self.assertEqual(self.library.books[-1].year, '1868')
        self.assertEqual(self.library.books[-1].status, '1')


if __name__ == '__main__':
    unittest.main()