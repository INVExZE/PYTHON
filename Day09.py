# Day 09 : FILE HANDLING IN PYTHON 

# EXAMPLE QUESTION

'''Q1. Write a program that reads a text 
file and prints its contents.'''

f = open('mytext.txt', 'r')
text = f.read()
print(text)
f.close()

'''Q2. Create a new text file and write 
some content into it.'''

g = open('mytext.txt', 'w')
g.write('Hello, world!')
g.close()

'''Q3. Read a CSV file and process its data.'''
import csv

with open('data.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)

file.close()


# PRACTICE QUESTION

'''1. Write a Python program to copy the contents of one text file into another'''

with open("test.txt") as f:
    with open("out.txt", "w") as f1:
        for line in f:
            f1.write(line)

'''2. '''

'''3. Implement a program that reads a text file and counts the
number of words and lines in it.'''

fname = input("Enter file name: ")
 
num_words = 0
 
with open(fname, 'r') as f:
    for line in f:
        words = line.split()
        num_words += len(words)
print("Number of words:")
print(num_words)


'''4. Create a function that takes a list of sentences and writes
them to a new text file, each on a new line.'''
def write_sentences_to_file(sentences, filename):
 
  with open(filename, "w") as f:
    for sentence in sentences:
      f.write(sentence + "\n")

sentences = ["This is the first sentence.", "This is the second sentence."]
write_sentences_to_file(sentences, "sentences.txt")
