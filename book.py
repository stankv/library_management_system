class Book:
    """
    The class representing the book.

    Attributes:
        id (int): ID of the book
        title (str): Title of the book
        author (str): Author of the book
        year (int): Year of publication
        status (int): Status of the book (1 = available, 0 = not available)

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
        self.id: int = id
        self.title: str = title
        self.author: str= author
        self.year: int = year
        self.status: int = status

    def switch_status_book(self):
        """
        Switch the status of the book (1 = available, 0 = was given)

        Returns:
            None
        """
        self.status = 1 - int(self.status)

    def __str__(self):
        if int(self.status) == 1:
            view_status = 'available'
        else:
            view_status = 'was given'
        return f"{self.id} Title: {self.title}, Author: {self.author}, Year: {self.year}, Status: {view_status}"

    def __repr__(self):
        return f"Title: {self.title}, Author: {self.author}, Year: {self.year}, Available: {self.status}"

    def __eq__(self, other):
        return self.title == other.title and self.author == other.author and self.year == other.year
