class LibraryBook:
    def __init__(self, title, author, publication_year):
        self.title = title
        self.author = author
        self.publication_year = publication_year
        self.is_checked_out = False

    def check_out(self):
        if not self.is_checked_out:
            self.is_checked_out = True
            return True
        return False

    def return_book(self):
        if self.is_checked_out:
            self.is_checked_out = False
            return True
        return False


class LibraryBookDelegator:
    def __init__(self, book):
        self.book = book

    def check_out(self):
        return self.book.check_out()

    def return_book(self):
        return self.book.return_book()

    def is_checked_out(self):
        return self.book.is_checked_out

    def get_book_info(self):
        return {
            'title': self.book.title,
            'author': self.book.author,
            'publication_year': self.book.publication_year,
            'is_checked_out': self.book.is_checked_out
        }


# Приклад використання
book = LibraryBook("The Great Gatsby", "F. Scott Fitzgerald", 1925)
delegator = LibraryBookDelegator(book)

print(delegator.check_out())
print(delegator.check_out())
print(delegator.return_book())
print(delegator.get_book_info())
