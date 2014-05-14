class Book:
    def __init__(self, title):
        self.title = title
        self.shelf = None
    def enshelf(self, shelf):
        if not self.shelf:
            shelf.books.append(self)
            self.shelf = shelf
        else:
            print("This book is already shelved")
    def unshelf(self):
        if self.shelf:
            self.shelf.books.remove(self)
            self.shelf = None

class Shelf:
    def __init__(self):
        self.books = []
    def listBooks(self):
        if self.books:
            for book in self.books:
                print(book.title)
        else:
            print("This shelf is empty")

class Library:
    def __init__(self):
        self.books = []
        self.shelves = []
    def addShelf(self):
        shelf = Shelf()
        self.shelves.append(shelf)
        return shelf
    def addBook(self, title):
        book = Book(title)
        self.books.append(book)
        return book
    def listBooks(self):
        if self.books:
            for book in self.books:
                print(book.title)
        else:
            print("This library is empty")



library = Library();
upperShelf = library.addShelf()
lowerShelf = library.addShelf()
theRigveda = library.addBook("The Rigveda")
theRigveda.enshelf(upperShelf)
theTipitaka = library.addBook("The Tipitaka")
theTipitaka.enshelf(upperShelf)
theQuran = library.addBook("The Quran")
theQuran.enshelf(upperShelf)
crimeAndPunishment = library.addBook("Crime and Punishment")
crimeAndPunishment.enshelf(lowerShelf)
learnPythonTheHardWay = library.addBook("Learn Python the Hard Way")
learnPythonTheHardWay.enshelf(lowerShelf)

print("The library contains %d books on %d shelves:" % (len(library.books), len(library.shelves)))
library.listBooks()

print("\nUpper shelf contents:")
upperShelf.listBooks()

print("\nLower shelf contents:")
lowerShelf.listBooks()

print("\nUnshelving LPTHW...")
learnPythonTheHardWay.unshelf()
print("Lower shelf contents:")
lowerShelf.listBooks()

print("\nEnshelving LPTHW...")
learnPythonTheHardWay.enshelf(upperShelf)
print("Upper shelf contents:")
upperShelf.listBooks()
