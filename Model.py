""" Implementation of Model class """

import pickle
import doctest
import Serialize as srz
from User import User
from Book import Book
from configuration.configParser import last_session_data_save, last_session_save_type

class Model:
    """ Class Model controls all operation on users and books in the library.

    Attributes:
        __users_list(list): List of library users.
        __books_list(list): List of books available in the library.
    """

    def __init__(self, filename, serialization_type):
        """ Initialize Model class

        Args:
            filename(str): Set name of the file which is used to upload
                information about library.
        """
        self.__users_list = []
        self.__books_list = []
        self.filename = filename
        self.serialization_type = serialization_type
        self.load()
        super().__init__()


    @property
    def user_list(self):
        """ list: Contains the list of library users. """
        return self.__users_list


    @property
    def book_list(self):
        """ list: Contains the list of books in a library. """
        return self.__books_list


    def create_user(self, username, age):
        """ Method  create user and add to user list.

        Args:
            username(str): Library user's name.
            age(int): User's age.
        Raises:
            Exception: if user with given username already exist.

        Examples:
            >>> model.create_user("Thor", 29)
            >>> model._show_list(model.user_list)
            ['Thor, age: 29']
            >>> model.create_user("Thor", 1000)
            Traceback (most recent call last):
            Exception: [ERROR]::The user already exists.
        """
        if self._is_username_exists(username):
            raise Exception("[ERROR]::The user already exists.")
        self.__users_list.append(User(username, age))


    def remove_user(self, username):
        """ Removes user form user list.

        Args:
            username(str): The name of the deleted user.
        Raises:
            Exception: if user with given username does not exist.

        Examples:
            >>> model.remove_user("Odin")
            Traceback (most recent call last):
            Exception: [ERROR]::There is no user with such name.
            >>> model.remove_user("Thor")
            >>> model._show_list(model.user_list)
            []
        """
        if not self._is_username_exists(username):
            raise Exception("[ERROR]::There is no user with such name.")
        self.__users_list = [user for user in self.__users_list if user.user_name != username]


    def add_book(self, title, author, year=None):
        """ Add new book to the library.

        Args:
            title(str): Book's title.
            author(str): Book's author.
            year(int, optional): The year when book was published
        Raises:
            Exception: if book with given title already exists.

        Examples:
            >>> model.add_book("Dialogs", "Seneka")
            >>> model.add_book("Dialogs", "Seneka")
            Traceback (most recent call last):
            Exception: [ERROR]::The book already exists.
            >>> model.add_book("Witchcraft: Special edition", "Angry Witcher")
            >>> model._show_list(model.book_list)
            ["'Dialogs', author:Seneka;", "'Witchcraft: Special edition', author:Angry Witcher;"]
        """
        if self._is_book_title_exists(title):
            raise Exception("[ERROR]::The book already exists.")
        self.__books_list.append(Book(title, author, year))


    def remove_book(self, title):
        """ Removes book from the library.

        Args:
            title(str): Book's title.
        Raises:
            Exception: if book with given title does not exist.

        Examples:
            >>> model.remove_book("Quantum mechanics: Second Edition")
            Traceback (most recent call last):
            Exception: [ERROR]::There is no book with shuch title.
            >>> model.remove_book("Dialogs")
            >>> model._show_list(model.book_list)
            ["'Witchcraft: Special edition', author:Angry Witcher;"]
        """
        if not self._is_book_title_exists(title):
            raise Exception("[ERROR]::There is no book with shuch title.")
        
        for user in self.__users_list:
            for b in user.book_list:
                if (b.book_name == title):
                    self.return_book(user.user_name, title)

        self.__books_list = [book for book in self.__books_list if book.book_name != title]


    def take_book(self, username, book_title):
        """ Adds the book to the user's book list.

        Args:
            username(str): User's name.
            book_title(str): Book's title.
        Raises:
            Exception: if user with given username does not exist
                        or book with given title does not exist.

        Examples:
            >>> model.take_book("Loki", "Witchcraft: Special edition")
            Traceback (most recent call last):
            Exception: [ERROR]::There is no such user or book.
            >>> model.create_user("Loki", 29)
            >>> model.take_book("Loki", "Witchcraft: Special edition")
            >>> print(model.book_list[0].owner)
            Loki, age: 29
            >>> model.user_list[1]._show_book_list()
            ["'Witchcraft: Special edition', author:Angry Witcher;"]
        """
        if not (self._is_book_title_exists(book_title) \
        and self._is_username_exists(username)):
            raise Exception("[ERROR]::There is no such user or book.")

        book_index = self.__books_list.index([item for item in self.__books_list \
                                             if item.book_name == book_title][0])
        user_index = self.__users_list.index([item for item in self.__users_list \
                                             if item.user_name == username][0])
        self.__books_list[book_index].owner = self.__users_list[user_index]
        self.__users_list[user_index].take_book(self.__books_list[book_index])


    def return_book(self, username, book_title):
        """ Returns book back to the library.

        Args:
            username(str): User's name.
            book_title(str): Book's title.
        Raises:
            Exception: if user with given username does not exist
                        or book with given title does not exist.
        Examples:
            >>> model.create_user("Thor", 29)
            >>> model.return_book("Thor", "Thunderstorm")
            Traceback (most recent call last):
            Exception: [ERROR]::There is no such user or book.
            >>> model.add_book("Thunderstorm", "Titan")
            >>> model.take_book("Thor", "Thunderstorm")
            >>> model.return_book("Thor", "Thunderstorm")
            >>> print(model.book_list[0].owner)
            None
            >>> model.user_list[0]._show_book_list()
            []
        """
        if not (self._is_book_title_exists(book_title) \
        and self._is_username_exists(username)):
            raise Exception("[ERROR]::There is no such user or book.")

        book_index = self.__books_list.index([item for item in self.__books_list \
                                             if item.book_name == book_title][0])
        self.__books_list[book_index].owner = None
        user_index = self.__users_list.index([item for item in self.__users_list \
                                             if item.user_name == username][0])
        self.__users_list[user_index].return_book(book_title)


    def feedback(self, book_title, rate):
        """ Sets rate for the particular book.

        Args:
            book_title(str): Book's title.
            rate(int) = Book rating points.
        Raises:
            Exception: if book with given title does not exist.
        """
        if not self._is_book_title_exists(book_title):
            raise Exception("[ERROR]::There is no book with given title.")
        index = self.__books_list.index([item for item in self.__books_list \
                                             if item.book_name == book_title][0])
        self.__books_list[index].rate = rate

    def load(self):
        """ Load information about library users and books

        Args:
            filename(str): Set name of the file which is used to upload
                information about library.
        """

        load_type = last_session_save_type()

        specifier = "rb" if load_type == srz.pickle_type else "r"
        try:
            with open(self.filename, specifier) as source:
                self.__users_list, self.__books_list = srz.load(source, load_type)
        except OSError:
            self.__users_list = []
            self.__books_list = []


    def save(self):
        """ Save information about library in text file.

        Args:
            filename(str): Set name of the file which is used to upload
                information about library.
        """
        specifier = "wb" if self.serialization_type == srz.pickle_type else "w"
        with open(self.filename, specifier) as target_file:
            srz.save([self.__users_list, self.__books_list], target_file, self.serialization_type)

        last_session_data_save(self.serialization_type)


    def _is_username_exists(self, username):
        user_name = [user for user in self.__users_list if user.user_name == username]
        return True if user_name else False


    def _is_book_title_exists(self, book_title):
        title = [book for book in self.__books_list if book.book_name == book_title]
        return True if title else False

    # this method created for test
    def _show_list(self, lst):
        return [str(item) for item in lst]


if __name__ == "__main__":
    doctest.testmod(extraglobs={"model": Model("storage", "pickle")})
