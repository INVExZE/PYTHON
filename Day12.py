# Day 12 : Revision Practice of FILE HANDLING

# PRACTICE QUESTIONS on CSV File Handling QUESTIONS.

'''Q1. CSV file handling to write a python program 
to add or insert records in a file data.csv'''

import csv

field = ["Roll. No","Name", "Class"]
f = open("data.csv","w")
d = csv.writer(f)
d.writerow(field)

ch = 'y'

while ch == 'y' or ch == 'Y':
    roll_no = int(input("Enter The Roll No: "))
    name = input("Enter The Name : ")
    Class = int(input("Enter The Class: "))
    rec = [roll_no, name, Class]
    d.writerow(rec)

    ch = input("Do you want to enter next record(y/n): ")
f.close()

f = open("data.csv", "r")
d = csv.reader(f)

for i in d :
    print(i)
f.close()


'''Q2 . Program to read all content of student.csv 
and display records of students scored more than 85.'''

import csv

f = open("student.csv","r")
d = csv.reader(f)
next(f)
print("Student scored more than 85")
print()

for i in d:
    if int(i[2])>85:
        print("Roll no: ",i[0])
        print("Name: ",i[1])
        print("Marks: ",i[2])
        print("----------------")

f.close()


'''Q3. Python program to calculate the sum of all 
the marks given in the csv file'''

import csv

f = open("student.csv", "r")
d = csv.reader(f)

next(f)
tot = 0

for i in d:
    tot = tot + int(i[2])

print("The Total Marks Obtained : ", tot)
f.close()


