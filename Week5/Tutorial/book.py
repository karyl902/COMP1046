#Academix Integrity statement
#Name: Zhenyi He
#Student ID: 521332
#Email: 521332@learning.eynesbury.edu.au
#This program is my own work as defined by the Academic Integrity
class Person:
    def __init__(self, forename: str, surname: str):
        self.__forename = forename  # given names
        self.__surname = surname  # family names

    @property
    def forename(self):
        return self.__forename

    @forename.setter
    def forename(self, forename):
        self.__forename = forename

    @property
    def surname(self):
        return self.__surname

    @surname.setter
    def surname(self, surname):
        self.__surname = surname

    def to_csv_str(self):
        return ','.join([self.forename, self.surname])

    def __str__(self):
        return self.forename + " " + self.surname


class Book:
    def __init__(self, title, author, date):
        self.__title = title
        self.__author = author
        self.__date = date

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
    def date(self):
        return self.__date

    @date.setter
    def date(self, date):
        self.__date = date

    def to_csv_str(self):
        return ','.join([
            self.title,
            self.author.to_csv_str(),
            self.date
        ])

    @classmethod
    def parse_csv(cls, csv_str: str):
        csv_str = csv_str.strip()
        values_from_csv = csv_str.split(',')
        title = values_from_csv[0]
        forename = values_from_csv[1]
        surname = values_from_csv[2]
        date = values_from_csv[3]
        author = Person(forename, surname)
        return cls(title, author, date)

    def __str__(self):
        return "".join([
            self.title,
            str(self.author),
            "(" + str(self.date) + ")"
        ])



