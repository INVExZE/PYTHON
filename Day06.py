# Day 6 : Functions in Python

# Exercise of Python

'''1. Given a list of numbers, create a function to find the sum
of all positive numbers"''' 
def theSum(aList):
    s = 0 
    for x in aList:
       if x > 0:
           s = s + x
    return s

aList = (-1 , 2, 3, 4)

sum = theSum(aList)
print("The sum of all positive numbers of the list are : ", sum)

'''2. Write a Python function to check if a given string is a palindrome"'''

string1= 'aIbohPhoBiA'
string1= string1.casefold()
rev_string1 = reversed(string1)

if list(string1) == list(rev_string1):
   print("The string is a palindrome.")
else:
   print("The string is not a palindrome.")


'''3. Implement a function that returns the factorial of a given number using recursion.'''

def recur_factorial(n):
   if n == 1:
       return n
   else:
       return n*recur_factorial(n-1)

num = 7

if num < 0:
   print("Sorry, factorial does not exist for negative numbers")
elif num == 0:
   print("The factorial of 0 is 1")
else:
   print("The factorial of", num, "is", recur_factorial(num))

'''4. Create a function to find the square of each element in a given list.'''

list_nums=[1, 2, 3, 4, 5]
print("Original list:",list_nums)
list_nums= [i**2 for i in list_nums]
print("Square elements:",list_nums)

'''5. Write a function to check if a number is even or odd and return "Even" or "Odd" accordingly"'''

def even_odd(number):
  if number % 2 == 0:
    return "Even"
  else:
    return "Odd"

print(even_odd(10)) 
print(even_odd(11)) 

'''6. Calculate the area of a triangle given its base and height using a function"'''

def calculate_area(base, height):
  return 0.5 * base * height


base = float(input('Enter the base side length: '))
height = float(input('Enter the height side length: '))


area = calculate_area(base, height)

print("Area of the triangle is:", area)

'''7. Create a function that takes a list of strings and returns the list sorted alphabetically.'''

str= ("python", "java", "tutoring", "Favtutor", "Machine Learning", "Studies", "Code", "Students")
x = sorted(str, reverse=False)
print(x)

'''8. Write a function that takes two lists and returns their intersection (common elements).'''

'''9. Implement a function to check if a given year is a leap year or not"'''

def CheckLeap(Year):  
    
  if((Year % 400 == 0) or  
     (Year % 100 != 0) and  
     (Year % 4 == 0)):   
    print("Given Year is a leap Year");  
  
  else:  
    print ("Given Year is not a leap Year")  

Year = int(input("Enter the number: "))  
CheckLeap(Year)  

'''10. Create a function that takes a number as input and prints its multiplication table.'''

def print_multiplication_table(number):
  
  for i in range(1, 11):
    print(f"{number} x {i} = {number * i}")

print_multiplication_table(5)