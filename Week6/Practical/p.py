#Academix Integrity statement
#Name: Zhenyi He
#Student ID: 521332
#Email: 521332@learning.eynesbury.edu.au
#This program is my own work as defined by the Academic Integrity
from abc import ABC, abstractmethod

class Employee(ABC):
    def __init__(self, first_name, last_name, employee_id):
        self.first_name = first_name
        self.last_name = last_name
        self.employee_id = employee_id
        self.base_salary = 0

    def set_base_salary(self, salary):
        self.base_salary = salary

    @abstractmethod
    def get_salary(self):
        pass

    @abstractmethod
    def get_staff_info(self):
        pass

class TeachingStaff(Employee):
    def __init__(self, first_name, last_name, employee_id, teaching_area, category):
        super().__init__(first_name, last_name, employee_id)
        self.teaching_area = teaching_area
        if 1 <= category <= 5:
            self.category = category
        else:
            print("Error: The category of a teaching staff should be between 1 and 5.")
            self.category = 0

    def get_salary(self):
        category_factor = self.category * 10 + 100
        factor = category_factor / 100
        salary = factor * self.base_salary
        return salary

    def get_staff_info(self):
        info = 'First name: ' + self.first_name
        info += '\nLast name: ' + self.last_name
        info += '\nEmployee ID: ' + str(self.employee_id)
        info += '\nArea of Expertise: ' + self.teaching_area
        info += '\nCategory: ' + str(self.category)
        info += '\nSalary: ' + str(self.get_salary())
        return info

class AdministrativeStaff(Employee):
    def __init__(self, first_name, last_name, employee_id, level):
        super().__init__(first_name, last_name, employee_id)
        if 1 <= level <= 3:
            self.level = level
        else:
            print("Error: The level of an administrative staff should be between 1 and 3.")
            self.level = 0

    def get_salary(self):
        level_factor = self.level * 15 + 100
        factor = level_factor / 100
        salary = factor * self.base_salary
        return salary

    def get_staff_info(self):
        info = 'First name: ' + self.first_name
        info += '\nLast name: ' + self.last_name
        info += '\nEmployee ID: ' + str(self.employee_id)
        info += '\nLevel: ' + str(self.level)
        info += '\nSalary: ' + str(self.get_salary())
        return info

class PaidEmployee(ABC):
    @abstractmethod
    def get_salary(self):
        pass

    @abstractmethod
    def get_staff_info(self):
        pass


class Person:
    def __init__(self, first_name, last_name, date_of_birth):
        self.first_name = first_name
        self.last_name = last_name
        self.date_of_birth = date_of_birth

    def get_name(self):
        full_name = "{0} {1}".format(self.first_name, self.last_name)
        return full_name

class Worker:
    def __init__(self, tfn, super_num, position):
        self.tfn = tfn
        self.super_num = super_num
        self.position = position

class Employee2(Person, Worker):
    def __init__(self, first_name, last_name, date_of_birth, tfn, super_num, employee_id, position):
        Person.__init__(self, first_name, last_name, date_of_birth)
        Worker.__init__(self, tfn, super_num, position)
        self.employee_id = employee_id

    def get_details(self):
        return (
            "Name: {}\n"
            "Date of Birth: {}\n"
            "------------------------\n"
            "Employee ID: {}\n"
            "Position: {}\n"
            "------------------------\n"
            "TFN: {}\n"
            "Super: {}".format(
                self.get_name(), 
                self.date_of_birth, 
                self.employee_id, 
                self.position, 
                self.tfn, 
                self.super_num
            )
        )

kim = Employee2('Kim', 'White', '12/08/2020', 4556655, 567, 
1121, 'Developer') 
print(kim.get_details()) 