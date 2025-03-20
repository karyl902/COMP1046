from book import Book

class Library:
     def __init__(self):
         self.books = []
         filename = 'library.csv'
         with open(filename) as file:
            lines = file.readlines()
            for line in lines:
                    book = Book.parse_csv(line)
                    self.__books.append(book)
                    pass
            pass
      #   print(self)
         pass
     #def __str__(self):
     #     return "\n".join([
     #          str(book) for book in self.__books
     #     ])
     pass
Library()

class Person:
    def __init__(self,forenames: str,surnames: str):
        self.forenames = forenames #given names
        self.surnames = surnames #family names
        pass
    
    @property
    def furenames(self):
            return self.__forenames

    @forenames.setter
    def forenames(self,forenames):
        self.__forenames = forenames
        pass

    @surnames
    def surnames(self):
        return self.__surnames
    @surnames.setter
    def surnames(self,surnames):
        self.__surnames = surnames
        pass
    pass


    @property
    def title(self):
        return self.__date
    
    @title.setter
    def title(self,date):
        self.__date = date
        pass

    def to_csv_str(self):
         return ','.join(
              self.title,
              self.author.to_csv_str(),
              self.date
         )
    @classmethod
    def parse_csv(cls,csv_str:str):
        values_from_csv = csv_str.split(',')
        csv_str = csv_str.strip(",")
        title = values_from_csv[0]
        forename = values_from_csv[1]
        surname = values_from_csv[2]
        date = values_from_csv[3]
        author = Person(forename,surname)
        return Book(title,author,date)
    def __str__(self):
        return "".join([
            self.title,
            str(self.author),
            "("+str(self.date)+")"
        ])
    pass


