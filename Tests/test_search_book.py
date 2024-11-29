import os
import unittest
from library import Library


class TestSearchBook(unittest.TestCase):

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

    def test_search_book_by_id(self):
        """Проверяет поиск книги по id"""
        self.library.add_book('Война и мир', 'Л.Н. Толстой', '1868')
        self.library.add_book('Три товарища', 'Э.М. Ремарк', '1936')
        self.library.add_book('Морской волк', 'Дж. Лондон', '1904')
        self.assertEqual(self.library.search_book_by_id('2').id, 2)
        self.assertEqual(self.library.search_book_by_id('2').title, 'Три товарища')
        self.assertEqual(self.library.search_book_by_id('2').author, 'Э.М. Ремарк')
        self.assertEqual(self.library.search_book_by_id('2').year, 1936)
        self.assertEqual(self.library.search_book_by_id('2').status, 1)

    def test_search_book_by_title(self):
        """Проверяет поиск книги по названию"""
        self.library.add_book('Война и мир', 'Л.Н. Толстой', '1868')
        self.library.add_book('Три товарища', 'Э.М. Ремарк', '1936')
        self.library.add_book('Морской волк', 'Дж. Лондон', '1904')
        book = self.library.search_books('title', 'Морской волк')
        self.assertEqual(book[0].id, 3)
        self.assertEqual(book[0].title, 'Морской волк')
        self.assertEqual(book[0].author, 'Дж. Лондон')
        self.assertEqual(book[0].year, 1904)
        self.assertEqual(book[0].status, 1)

    def test_search_book_by_author(self):
        """Проверяет поиск книги по автору"""
        self.library.add_book('Война и мир', 'Л.Н. Толстой', '1868')
        self.library.add_book('Три товарища', 'Э.М. Ремарк', '1936')
        self.library.add_book('Морской волк', 'Дж. Лондон', '1904')
        book = self.library.search_books('author', 'Дж. Лондон')
        self.assertEqual(book[0].id, 3)
        self.assertEqual(book[0].title, 'Морской волк')

    def test_search_book_by_year(self):
        """Проверяет поиск книги по году издания"""
        self.library.add_book('Война и мир', 'Л.Н. Толстой', '1868')
        self.library.add_book('Три товарища', 'Э.М. Ремарк', '1936')
        self.library.add_book('Морской волк', 'Дж. Лондон', '1904')
        book = self.library.search_books('year', '1904')
        self.assertEqual(book[0].id, 3)
        self.assertEqual(book[0].title, 'Морской волк')


    if __name__ == '__main__':
        unittest.main()
