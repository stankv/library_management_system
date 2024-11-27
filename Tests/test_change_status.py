import os
import unittest
from library import Library


class TestChangeStatus(unittest.TestCase):

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

    def test_change_status_book_in_library(self):
        """Тестирует функцию change_status_book на объекте Library"""
        self.library.add_book('Война и мир', 'Л.Н. Толстой', '1868')
        self.library.add_book('Три товарища', 'Э.М. Ремарк', '1936')
        self.library.change_status_book(self.library.books[0])
        self.assertEqual(self.library.books[0].status, 0)

    def test_change_status_book_in_file(self):
        """Тестирует функцию change_status_book на файле"""
        self.library.add_book('Война и мир', 'Л.Н. Толстой', '1868')
        self.library.add_book('Три товарища', 'Э.М. Ремарк', '1936')
        self.library.change_status_book(self.library.books[0])
        with open(self.library.file_db, "r", encoding="utf-8") as f:
            lines = f.readlines()
        self.assertEqual(lines[0], '1;Война и мир;Л.Н. Толстой;1868;0\n')


if __name__ == '__main__':
    unittest.main()
