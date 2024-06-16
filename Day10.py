# DAY 10 : INTRODUCTION TO OOPS IN PYTHON

# EXAMPLE QUESTIONS


'''Q1. Create a class to represent a basic 
calculator with add, subtract, multiply, and 
divide methods.'''

class Calculator :
    def add(self, a , b):
        return a + b 
    def subs(self, a , b):
        return a - b 
    def multiply(self, a , b):
        return a * b 
    def quotient(self, a , b):
        return a // b 
    def remiander(self, a , b):
        return a % b 
    
a = int(input("Enter 1st Number : "))
b = int(input("Enter 2nd Number : "))

calculator = Calculator()

result = calculator.add(a, b)
print(f"The Addition of '{a} + {b}' is {result}")

result = calculator.subs(a, b)
print(f"The Substraction of '{a} - {b}' is {result}")

result = calculator.multiply(a, b)
print(f"The Multiply of '{a} * {b}' is {result}")

result = calculator.quotient(a, b)
print(f"The Division of '{a} / {b}' is {result}")

'''2. Create a class to represent a book with attributes 
like title, author, and publication year.'''

class Book:
    title = ()
    author = ()
    year = ()

    def info(self):
        print(f"The Title of the Book is : '{self.title}' 
              whose author is '{self.author}' and the Publication 
              year of the book is  '{self.year}'\n" )

a = Book()
a.author = "Sanjay Singh"
a.title = "The Great Indian History."
a.year = 2002

b = Book()
b.author = "Ankit Kumar"
b.title = "Social Marketing"
b.year = 2020

a.info()
b.info()

'''Q3. Define a class for a cirle with methods to 
calculate its area and circumference.'''

class Circle:
    def area(self, radius) :
        return 3.14 * radius ** 2
    def circumference(self, radius):
        return 2 * 3.14 * radius
    
radius = float(input("Enter the radius of the circle : "))

circle = Circle()

result1 = circle.area(radius)
print(f"The Area of the Circle with radius '{radius}' is {result1}")

result1 = circle.circumference(radius)
print(f"The Circumference of the Circle with radius '{radius}' is {result1}")


# PRACTICE QUESTIONS

'''1. Create a class to represent a Student with attributes like name, age and grades'''

class Student:
    name = ()
    age = ()
    grades = ()

    def info(self):
        print(f"The Name of the Student is : '{self.name}' whose age is '{self.age}' and the grades he scored is '{self.grades}'\n" )

a = Student()
a.name = "Sanjay Singh"
a.age = 20
a.grades = "A"

a.info()


'''2. Given a CSV file with employee details (name, position, salary), create a class to represent an Employee.'''

import csv
with open("employee.csv","r", newline = '') as p :

    data1 = csv.reader(p)
    for r in data1 :
        print(r)

'''3. '''





