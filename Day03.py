# Day 3 : PYTHON : conditional statements and loops

# EXAMPLE QUESTIONS

'''Q1. Write a program that checks if a given 
number is positive, negative, or zero.'''

num = int(input("Enter A Number : "))

if(num > 0) :
    print("The Number Entered is 'POSITIVE'.")
elif(num < 0) :
    print("The Number Entered is 'NEGATIVE'.")
else :
    print("The Number Entered is 'ZERO'.")

'''Q2. Create a loop that prints the first 
10 even numbers.'''
maximum = 10

for number in range(1, maximum + 1):
    
    if number % 2 == 0 :
        print(number)

'''Q3. Implement a program that finds the largest 
number in a list.'''
list1 = [1, 0, 4, 5, 100]

print("Largest element of the list is:", max(list1))



# PRACTICE PROBLEM 

'''1. Create a program that takes a year as input and checks if it is a leap year or not.'''

year = int(input("Enter a year: "))

if (year % 4 == 0) and (year % 100 != 0):
    print(year, "is a leap year.")
elif (year % 400 == 0):
    print(year, "is a leap year.")
else:
    print(year, "is not a leap year.")


'''2. Given a list of integers, find all the even 
numbers and store them in a new list.'''

list = [10, 21, 4, 45, 66, 93]
 
for num in list:
 
    if num % 2 == 0:
        print(num, end=" ")


'''3. Write a Python program to check if a given 
number is a prime number.'''

num = int(input("Enter a number: "))

if num == 1:
    print(num, "is not a prime number")
elif num > 1:
   
   for i in range(2,num):
       if (num % i) == 0:
           print(num,"is not a prime number")
           print(i,"times",num//i,"is",num)
           break
   else:
       print(num,"is a prime number")
       

else:
   print(num,"is not a prime number")


'''4. Create a program that generates the Fibonacci 
sequence up to a given number of terms)'''

num = int(input("Enter the Number : "))
n1, n2 = 0, 1
print("Fibonacci Series:", n1, n2, end=" ")
for i in range(2, num):
    n3 = n1 + n2
    n1 = n2
    n2 = n3
    print(n3, end=" ")

print()


'''5. Given a list of names, print all names starting 
with the letter 'A'.'''

names = [
    'Aakash', 'Ayush','Bablu',
    'Baskey','Sathak','Karan',
    'Jeewanshu','Ankit']

for name in names:
    if name[0] == "A":
        print(name)


'''6. Implement a program that prints the multiplication table
of a given number.'''

num = 12

num = int(input("Display multiplication table of? "))

for i in range(1, 11):
   print(num, 'x', i, '=', num*i)


'''7. Write a program that calculate the factorial of a given number.'''

num = 7

num = int(input("Enter a number: "))

factorial = 1

if num < 0:
   print("Sorry, factorial does not exist for negative numbers")
elif num == 0:
   print("The factorial of 0 is 1")
else:
   for i in range(1,num + 1):
       factorial = factorial*i
   print("The factorial of",num,"is",factorial)


'''8. Create a loop that prints all prime 
numbers between 1 and 50.'''

lower = 1
upper = 50

print("Prime numbers between", lower, "and", upper, "are:")

for num in range(lower, upper + 1):
   # all prime numbers are greater than 1
   if num > 1:
       for i in range(2, num):
           if (num % i) == 0:
               break
       else:
           print(num, end = " ")


'''9. Given a list of words, count the number of 
words with more than five characters.'''

n = 5
str = ["Sanjay", "Aakash", "Bablu", "Aman"]
new_list = []
text = str.split(" ")
for x in text:
	if len(x) > n:
		new_list.append(x)
print(new_list)


'''10. Calculate the sum of digits of a given 
number.'''

num = input("Enter Number: ")
sum = 0

for i in num:
    sum = sum + int(i)

print(sum)


