# Day 7 : PYTHON : String Manipulation

# EXAMPLE QUESTIONS

'''Q1. Create a program that checks if 
a given string is a palindrome.'''

given = 'aIbohPhoBiA'
given = given.casefold()

rev_str = reversed(given)

if list(given) == list(rev_str):
   print("The string is a palindrome.")
else:
   print("The string is not a palindrome.")


'''Q2. Write a function to count the number 
of vowels in a given string.'''

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


'''Q3. Write a function to count the number of 
vowels in a given string.'''
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


# PRACTICE QUESTIONS 
'''1. Given a list of words, concatenate them into a single string separated by spaces.'''
