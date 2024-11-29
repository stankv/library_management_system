class Book:
    """
    The class representing the book.

    Attributes:
        __id (int): ID of the book
        __title (str): Title of the book
        __author (str): Author of the book
        __year (int): Year of publication
        __status (int): Status of the book (1 = available, 0 = not available)

    Methods:
        switch_status_book(): Switch the status of the book
    """
    def __init__(self, id: int, title: str, author: str, year: int, status: int = 1):
        """
        Constructor. Sets the attributes of the book

        Args:
            id (int): ID of the book
            title (str): Title of the book
            author (str): Author of the book
            year (int): Year of publication
            status (int): Status of the book (1 = available, 0 = was given)
        """
        self.__id: int = id
        self.__title: str = title
        self.__author: str= author
        self.__year: int = year
        self.__status: int = status

    def switch_status_book(self):
        """
        Switch the status of the book (1 = available, 0 = was given)

        Returns:
            None
        """
        self.status = 1 - int(self.status)

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, value):
        if int(value) < 1:
            raise ValueError("ID must be greater than or equal to 1")
        self.__id = value

    @property
    def title(self):
        return self.__title

    @title.setter
    def title(self, title):
        self.__title = title

    @property
    def author(self):
        return self.__author

    @author.setter
    def author(self, author):
        self.__author = author

    @property
    def year(self):
        return self.__year

    @year.setter
    def year(self, year):
        self.__year = year

    @property
    def status(self):
        return self.__status

    @status.setter
    def status(self, status):
        self.__status = status

    def __str__(self):
        if int(self.status) == 1:
            view_status = 'available'
        else:
            view_status = 'was given'
        return f"{self.id} Title: {self.title}, Author: {self.author}, Year: {self.year}, Status: {view_status}"

    def __repr__(self):
        return f"title={self.title}, author={self.author}, year={self.year}, status={self.status}"

    def __eq__(self, other):
        return self.title == other.title and self.author == other.author and self.year == other.year
