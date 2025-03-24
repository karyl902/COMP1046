#Academix Integrity statement
#Name: Zhenyi He
#Student ID: 521332
#Email: 521332@learning.eynesbury.edu.au
#This program is my own work as defined by the Academic Integrity

from book import Book

class Library:
     def __init__(self):
         self.__books = list()
         filename = 'library.csv'
         with open(filename) as file:
            lines = file.readlines()
            for line in lines:
                book = Book.parse_csv(line)
                self.__books.append(book)
                pass
            pass
         print(self)
         pass
     def __str__(self):
         return "\n".join([
             str(book) for book in self.__books
          ])
     pass

Library()