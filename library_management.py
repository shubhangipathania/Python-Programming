#Library Management
class Library:
    def __init__(self):
        self.books=[]
        self.nobooks=0

    def addBook(self, book):
        self.books.append(book)
        self.nobooks=len(self.books)

    def showInfo(self):
        print(f"The Library has {self.nobooks} books named {self.books}.")


l1=Library()
l1.addBook("The 5Am Club")
l1.addBook("Better Than The Movies ")
l1.addBook("The Last Queen")
l1.showInfo()