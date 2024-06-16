# STRINGS IN PYTHON   || STRING SLICING

name = "Sanjay"

print(name[0])
print(name[1])
print(name[2])
print(name[3])


names = "Sanjay, Ankit, Aakash"
len1 = len(names)

print("The length of all the names is : " , len1)

#It prints strings from 0 to n - 1 
print(names[0:15])
print(names[5:15])
print(names[:6])
print(names[1:-8])
print(names[0:len(names)-8])
print(names[-1:-8])
print(names[-8:-1])


# FUNCTIONS OF STRINGS 
# STRINGS ARE IMMUTABLE

sample = "Sanjay"

# All letter upper case.
print(sample.upper())

# All letter lower case 
print(sample.lower())

# Strip the end tail recursive part
a = "Sanjay !!!!!"
print(a)
print(a.rstrip("!"))

# Replace the word

print("Before replacing : ", a)
print(a.replace("Sanjay", "Singh"))

#Capitalize the first index

heading = "heading of the newspaper"
print(heading.capitalize())




# f-STRINGS in PYTHON

letter = "Hey my name is {1} and I am from {0}"
country = "India"
name = "Sanjay"

# Conventional way of writing
print(letter.format(country, name))

# Using f-String
print(f"Hey my name is {name} and I am from {country}")

# To Print{} in Output use DOUBLE {{}}
print(f"We use f-strings like this: Hey my name is {{name}} and I am from {{country}}")


price = 49.09999
txt = f"For only {price:.2f} dollars!"
print(txt)

# print(txt.format())
print(type(f"{2 * 30}"))
