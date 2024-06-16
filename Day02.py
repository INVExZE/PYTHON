# Day 2 : PYTHON : Varibales and Data Types

# EXAMPLE QUESTIONS

'''Q1. Create variables for storing a person's name, age, and
average test score'''

name = input("Enter the name : ")
age = input("Enter the age : ")
score  = input("Enter the average test score : ")

print("The name of the person is : ", name)
print("The age of the person is : ", age)
print("The average test score of the person is : ", score)


'''Q2. Concatenate two strings and print the result.'''

print('first ' + ' second')


'''Q3. Create a list of fruits and access elements using indexing.'''

fruits = ['Apple', 'Banana', 'Mango', 'Cherry', 'Grapes']

print(fruits[2])
print(fruits[4])
print(fruits[1])




# PRACTICE QUESTIONS

'''1. Given a list of numbers, find the sum and average.'''

L = [4, 5, 1, 2, 9, 7, 10, 8]

print("The Numbers of the List are : ", L)

count = sum(L)
 
avg = count/len(L)
 
print("sum = ", count)
print("average = ", avg)

'''2. Create a program that takes a temperature in Celsius and
converts it to Kelvin.'''

celsius = int(input("Enter Temp. in Celcius : "))
Convert1 = (celsius + 273) 
print("The Converted Temp. in Kelvin is : ", Convert1 )


'''3. Implement a program that checks if a given string is a
palindrome.'''
given = 'aIbohPhoBiA'
given = given.casefold()

rev_str = reversed(given)

if list(given) == list(rev_str):
   print("The string is a palindrome.")
else:
   print("The string is not a palindrome.")


'''4. Create a function to reverse a given string.'''
def reverse(s):
    str = ""
    for i in s:
        str = i + str
    return str
 
s = "Hello World"
 
print("The original string is : ", end = "")
print(s)
 
print("The reversed string(using loops) is : ", end = "")
print(reverse(s))


'''5. Given a list of names, concatenate them into a 
single string separated by spaces'''
names = ['Abhishek', 'Ankit', 'Ayush', 'Bablu', 'Aakash']

print(" ".join(names)) 


'''6. Write a Python program to check if a given string is a
pangram (contains all letters of the alphabet).'''
import string

def ispangram(str):
	alphabet = "abcdefghijklmnopqrstuvwxyz"
	for char in alphabet:
		if char not in str.lower():
			return False

	return True
	
string = input("Enter the sentence : ")
if(ispangram(string) == True):
	print("Yes")
else:
	print("No")
	

'''7. Calculate the area and circumference of a circle given its
radius.'''

radius = float(input("Enter the radius of the circle : "))
print("The area of the circle is : ", 3.14 * radius * radius )
print("The circumference of the circle is : ", 3.14 * 2 * radius )

'''8. Implement a program that converts a given number of
minutes into hours and minutes'''

minutes = int(input("Enter the Minutes : "))

print("The Minutes into Hours is : ", minutes / 24 )
print("The Minutes into Seconds is : ", minutes * 60 )


'''9. Create a function to count the number of vowels in a
given string.'''

String = input('Enter the string :')
count = 0

String = String.lower()
for i in String:
    if i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u':
        
        count+=1

if count == 0:
    print('No vowels found')
else:
    print('Total vowels are :' + str(count))

'''10. '''



