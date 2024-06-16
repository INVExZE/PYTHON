
#                           EXCEPTION HANDLING

# In this case if we give a string value in input 
# then the code below the loop doesn't work. 
# So to overcome this we use try : and except : 


a = input("Enter the number: ")
print(f"Multiplication table of {a} is: ")
try:
  for i in range(1, 11):
    print(f"{int(a)} X {i} = {int(a)*i}")
except:
  print("Invalid  Input!")

print("Some imp lines of code")
print("End of program")


# We can use two except in try for multiple
# Case checks.

try:
    num = int(input("Enter an integer: "))
    a = [6, 3]
    print(a[num])
except ValueError:
    print("Number entered is not an integer.")
    
except IndexError:
  print("Index Error")



#                           FINALLY CLAUSE

# Finally Caluse is used to run a block of code at any cost

  try:
    l = [1, 5, 6, 7]
    i = int(input("Enter the index: "))
    print(l[i])
    
  except:
    print("Some error occurred")
    

  finally:
    print("I am always executed")
  

# In case of Function after the return block NO CODE GETS EXECTUTED.
#  SO to execute the BLOCK OF CODE WE USE FINALLY.

def func1():
  try:
    l = [1, 5, 6, 7]
    i = int(input("Enter the index: "))
    print(l[i])
    return 1
  except:
    print("Some error occurred")
    return 0

  finally:
    print("I am always executed")

print("I am always executed after code.")


x = func1()
print(x)