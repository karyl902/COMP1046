#Academix Integrity statement
#Name: Zhenyi He
#Student ID: 521332
#Email: 521332@learning.eynesbury.edu.au
#This program is my own work as defined by the Academic Integrity

#Task1
class Person:
    def __init__(self, names, age):
        if len(names) < 1:
            print("Error: The names list must contain at least one element.")
            return
        if age < 0:
            print("Error: Age must be 0 or greater.")
            return
        self.names = names
        self.age = age
        self.initial_age = age

    def getFullName(self):
        return ' '.join(self.names)

    def birthday(self):
        self.age = self.age + 1

    def getAge(self):
        return self.age

    def getNameHarvardFormat(self):
        if len(self.names) == 1:
            return self.names[0] + ", "
        last_name = self.names[-1]
        initials = ''.join([name[0] for name in self.names[:-1]])
        return last_name + ", " + initials
#Task 1.2
    def __str__(self):
        return "Person: Name='" + self.getFullName() + "', Age=" + str(self.initial_age)
#Task 2.2
    def __repr__(self):
        return self.getNameHarvardFormat()
#Task 2



class Book:
    def __init__(self, authors, title, publisher, publish_year, publish_place):
        if len(authors) < 1:
            print("Error: The authors list must contain at least one author.")
            return
        self.authors = authors
        self.title = title
        self.publisher = publisher
        self.publish_year = publish_year
        self.publish_place = publish_place

    def displayAuthors(self):
        print(self.authors)

    def getHarvardReference(self):
        author_refs = []
        for i, author in enumerate(self.authors):
            author_ref = author.getNameHarvardFormat()
            if i == len(self.authors) - 1 and i > 0:
                author_ref = " & " + author_ref
            author_refs.append(author_ref)
        author_str = ", ".join(author_refs)
        return author_str + " " + str(self.publish_year) + ", " + self.title + ", " + self.publisher + ", " + self.publish_place + "."

    # Task 2.2
    def __str__(self):
        return self.getHarvardReference()



#Task 1 test
programmer = Person(['Augusta', 'Ada', 'King'], 36)
print(programmer.getFullName(), 'is', programmer.getAge())
programmer.birthday()
print(programmer.getFullName(), 'is', programmer.getAge())
print(programmer.getNameHarvardFormat())
print(programmer)
#Task 2 test
programmer = Person(['Augusta', 'Ada', 'King'], 36)
engineer = Person(['Charles', 'Babbage'], 50)
actualAuthor = Person(['Sydney','Padua'], 30)
book = Book([programmer, engineer, actualAuthor],
 'The Thrilling Adventures of Lovelace and Babbage',
 'Penguin Books', 2015, 'Westminster')
print(book)
book.displayAuthors()
