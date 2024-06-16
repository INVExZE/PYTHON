# Input from user
input("Enter your name : ")

name = input("Enter your Name : ")
print("Welcome to the course, ", name)


# Takes input as string so any data set can be printed
name1 = input("Enter Any Data : ")
print(type(name1), name1)

# Takes input only as integer and gives output
name2 = int(input("Enter Any Number : "))
print(type(name2), name2)

#Python print() with end Parameter
print('Good Morning!', end = ' ')
print('Its rainy today.')

#Python print() with sep parameter
print('New Year', 2023, 'See you soon!', sep = '. ')



# OUTPUT FORMATTING
x = 5 
y = 10

print('The value of x is {} and y is {}'.format(x,y))

#Python User Input 
# using input() to take user input
num = input('Enter a number: ')

print('You Entered:', num)

print('Data type of num:', type(num))
