# Day 5 : PYTHON : Functions

# EXAMPLE QUESTIONS

'''1. Write a function to calculate the area 
of a circle given its radius.'''
import math

def circle_area(radius):

  if radius < 0:
    return "Error: Radius cannot be negative."
  else:
    return math.pi * radius * radius

radius = int(input("Enter The Radius : "))

area = circle_area(radius)
print("The area of a circle is: ", area)

'''2. Create a function to check if a number 
is prime.'''

def is_prime(n):
  
  if n <= 1:
    return False

  for i in range(2, int(n**0.5) + 1):
    if n % i == 0:
      return False

  return True

'''3. Create a function to check if a number is prime.'''
def is_prime(n):
  
  if n <= 1:
    return False

  for i in range(2, int(n**0.5) + 1):
    if n % i == 0:
      return False

  return True

n = int(input("Enter the Number : "))
prime = is_prime(n)
print("Is the number 'PRIME': ", prime)


