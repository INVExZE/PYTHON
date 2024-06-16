# Example Question.

'''Q1. Write a python program to print "Hello World"'''
print("Hello World!")

'''Q2. Calculate the sum of two numbers entered by the user.'''
num1 = int(input("Enter 1st Number : "))
num2 = int(input("Enter 2nd Number : "))

sum = num1 + num2 
print("The Sum of two numbers is : ", sum)

'''Q3. Convert the temperature from Celsius to Fahrenheit'''
a = int(input("Enter Temp. in Celcius : "))
Convert1 = (a * 9/5) + 32 
print("The Converted Temp. in Farhenheit is : ", Convert1 )

b = int(input("Enter Temp. in Farhenheit : "))
Convert2 = (b - 32) * 5/9
print("The Converted Temp. in Celcius is : ", Convert2 )


# PRACTICE QUESTIONS 

'''1. Write a Python program to calculate the area of a 
rectangle given its length and width.'''
length = 24 
width = 23 

print("The Area of the Rectangle is : ", length * width )


'''2. Create a program that takes a user's name and age as 
input and prints a greeting message.'''
a = input("Enter your name : ")
b = input("Enter your age : ")

print("I hope you're doing well, ", a)


'''3. Write a program to check if a number is even or odd'''
num3 = int(input("Enter a number: "))
if (num3 % 2) == 0:
   print("{0} is Even".format(num3))
else:
   print("{0} is Odd".format(num3))


'''4. Given a list of numbers, find the maximum and minimum 
values.'''
a = [15,58,30,97]
x = min(a)
y = max(a)
print("The List of Numbers is: ", a)
print("The Smallest element is {} and the Largest element is {}".format(x, y))


'''5. Create a Python function to check if a 
given string is a palindrome.'''
given = 'aIbohPhoBiA'
given = given.casefold()

rev_str = reversed(given)

if list(given) == list(rev_str):
   print("The string is a palindrome.")
else:
   print("The string is not a palindrome.")


'''6. Calculate the compound interest for a given 
principal amount, interest rate, and time period.'''
import math  
def compound_interest(p,r,t):   
    amt = p * (math.pow((1 + (r/100)),t))
    print("Compound Amount: ",amt)
    CI = amt - p
    return CI

p = float(input("Enter Principal Amount: "))
r = float(input("Enter Rate of Interest: "))
t = float(input("Enter Time Period in years: "))

print("Compound interest is",compound_interest(p,r,t))



'''7. Write a program that converts a given number 
of daysinto years, weeks, and days.'''
day = int(input("Enter the days : "))
year = (day//365)
weeks = (day % 365)//7
days = day - ((year * 365) + (weeks*7))

print("Year : ",year)
print("weeks : ",weeks)
print("Day : ",days)


'''8. Given a list of integers, find the sum of all positive numbers.'''



'''9. Create a program that takes a sentence as 
input and counts the number of words in it.'''
string = input("Enter string:")
char = 0
word = 1
for i in string:
      char = char + 1
      if(i == ' '):
            word = word + 1
print("Number of words in the string:", word)

print("Number of characters in the string:", char)


'''10. Implement a program that swaps the 
values of two variables.'''
s = 5
w = 10

temp = s
s = w
w = temp

print('The value of x after swapping: {}'.format(s))
print('The value of y after swapping: {}'.format(w))
