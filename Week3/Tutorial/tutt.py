class Page:
    def __init__(self, words =list()):
        self.__words = list()
        return
    def write(self, words:list):
        for word in words:
            self.__words.append(word)
            pass
        return
    def erase(self, words:list):
        for word in words:
            self.__words.remove(word)
            pass
        return
    pass
class Book:
    def __init__(self, pages: list):
        self.__pages = pages
        return
    def add(self,page: Page):
        self.__page.append(page)
        return
    def remove(self,page: Page):
        self.__page.remove(page)
        return
    def add(self, page: Page, inex: int):
        return
    def read(self):
        return
    pass
class shell:
    def __init(self):
     return
    def add(self, book: Book):
        return
    def remove(self, book: Book):
        return
    pass
class Bookcase:
    def __init__(self):
     return
    def add(self, book: Book, shelf: int):
        return
    def remove(self, book: Book):
        return
    pass

