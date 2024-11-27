import os
import unittest
from library import Library
from book import Book

class TestDeleteBook(unittest.TestCase):

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

    def test_delete_book_from_library(self):
        """Проверяет удаление книги из библиотеки"""
        self.library.add_book('Война и мир', 'Л.Н. Толстой', '1868')
        self.library.add_book('Три товарища', 'Э.М. Ремарк', '1936')
        self.library.add_book('Морской волк', 'Дж. Лондон', '1904')
        book = self.library.search_book_by_id('1')
        self.library.delete_book(book)
        self.assertEqual(len(self.library.books), 2)
        self.assertEqual(self.library.books[0].id, 2)
        self.assertEqual(self.library.books[1].id, 3)

    def test_delete_book_from_file(self):
        """Проверяет удаление книги из файла"""
        self.library.add_book('Война и мир', 'Л.Н. Толстой', '1868')
        self.library.add_book('Три товарища', 'Э.М. Ремарк', '1936')
        self.library.add_book('Морской волк', 'Дж. Лондон', '1904')
        book = self.library.search_book_by_id('1')
        self.library.delete_book(book)
        with open(self.library.file_db, "r", encoding="utf-8") as f:
            lines = f.readlines()
        self.assertEqual(len(lines), 2)
        self.assertEqual(lines[0], '2;Три товарища;Э.М. Ремарк;1936;1\n')
        self.assertEqual(lines[1], '3;Морской волк;Дж. Лондон;1904;1\n')


if __name__ == '__main__':
    unittest.main()