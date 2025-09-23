'''
Question:
Design a library system where:
'''

class Library:
    def __init__(self):
        self.books = {}   # {title: [author, __copies]}

    def add_book(self, title, author, copies):
        self.books[title] = [author, copies]  # copies kept private internally
        print(f"Added {title} to the library")

    def __get_copies(self, title):   # private helper method
        return self.books[title][1]

    def __set_copies(self, title, copies):   # private helper method
        self.books[title][1] = copies

    def borrow_book(self, title):
        if title in self.books:
            if self.__get_copies(title) > 0:
                self.__set_copies(title, self.__get_copies(title) - 1)
                print(f"You borrowed {title}")
            else:
                print(f"{title} is not available")
        else:
            print(f"{title} not found in the library")

    def return_book(self, title):
        if title in self.books:
            self.__set_copies(title, self.__get_copies(title) + 1)
            print(f"You returned {title}")
        else:
            print(f"{title} does not belong to this library")

    def show_books(self):
        print("\n Available Books:")
        for title, (author, copies) in self.books.items():
            print(f"{title} by {author} - Copies: {copies}")


# ------------------- Testing -------------------
lib = Library()
lib.add_book("Python Basics", "Guido van Rossum", 2)

lib.show_books()
lib.borrow_book("Python Basics")
lib.borrow_book("Python Basics")
lib.borrow_book("Python Basics")  # not available
lib.return_book("Python Basics")
lib.show_books()



