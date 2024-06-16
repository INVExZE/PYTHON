# Day 07 : LISTS AND TUPLES IN PYTHON 

# EXAMPLE QUESTION

'''Q1. Given a list of numbers, find 
the sum and average using built-in functions.'''

import statistics
L = [4, 5, 1, 2, 9, 7, 10, 8]

sum1 = sum(L)
 
avg = statistics.mean(L)
 
print("sum = ", sum1)
print("average = ", avg)

'''Q2. Create a list of fruits and 
add a new fruit to the list.'''

fruits = []
for i in range(1,5):
    fruits.append(input(f"Name of Fruit {i}:  "))
print(fruits)

'''Q3. Access elements in a tuple using indexing'''
languages = ('Python', 'Swift', 'C++')

print(languages[0])   
print(languages[2])

# PRACTICE QUESTIONS

'''1. Given two lists of numbers, concatenate 
them into a single list.'''

list3 = [1, 4, 5, 6, 5]
list4 = [3, 5, 7, 2, 5]

list3 = list3 + list4
 
print ("Concatenated list using + : "
                + str(list3))

'''2. Write a program that finds the largest and 
smallest elements in a list.'''
lst = []
num = int(input('How many numbers: '))

for n in range(num):
    numbers = int(input('Enter number : '))
    lst.append(numbers)

print("Maximum element in the list is :", max(lst)) 
print("Minimum element in the list is :", min(lst))


'''3. Implement a function that takes a list of 
numbers and returns a new list with the squared values$'''
list_nums=[1, 2, 3, 4, 5]
print("Original list:",list_nums)
list_nums= [i**2 for i in list_nums]
print("Square elements:",list_nums)


'''4. Create a program that finds the common elements
between two lists and stores them in a new list$'''
def common_member(a, b):
    result = [i for i in a if i in b]
    return result
 
a = [1, 2, 3, 4, 5]
b = [5, 6, 7, 8, 9]
 
print("The common elements in the two lists are: ")
print(common_member(a, b))

'''5. Given a list of words, find the word with the maximum
length and its length.'''
list = ['gfg', 'is', 'best', 'for', 'greed']
 
print("The original list : " + str(list))

res = max(list, key = len)
print("Maximum length string is : " + res)

'''6. Write a Python program to count the occurrences 
of each element in a given list'''

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]  
count = my_list.count(5)  
print(count)  

'''7. Given a list of names, remove all duplicate names and
print the unique names$'''

'''8. Create a function that takes a list of strings and returns
the list sorted by the length of the strings.'''
my_numbers = [10, 8, 3, 22, 33, 7, 11, 100, 54]
my_numbers.sort()

print(my_numbers)

'''9. Write a program that checks if a given list 
is sorted in ascending order.'''
list = [10, 4, 5, 8, 10]
 
print ("Original list : " + str(list))

flag = 0
list1 = list[:]
list1.sort()
if (list1 == list):
    flag = 1
     
if (flag) :
    print ("Yes, List is sorted.")
else :
    print ("No, List is not sorted.")


'''10. Implement a function that takes two lists and returns their
union (all unique elements from both lists'''

l1 = []
num1 = int(input('Enter size of list 1: '))
for n in range(num1):
    numbers1 = int(input('Enter any number:'))
    l1.append(numbers1)
 
l2 = []
num2 = int(input('Enter size of list 2:'))
for n in range(num2):
    numbers2 = int(input('Enter any number:'))
    l2.append(numbers2)
 
union = list(set().union(l1,l2))
 
print('The Union of two lists is:',union)