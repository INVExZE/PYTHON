#To print each letter of name
name = 'Abhishek'
for i in name:
  print(i)
  if(i =="b"):
    print("This is something special!")
    
#To print each list
colors = ["Red", "Green", "Blue", "Yellow"]
for color in colors:
  print(color)
  for i in color:
    print(i)

#To print numbers from 0 to 4.
for k in range(5):
  print(k)
#To print numbers from 0 to 5.
  print(k + 1)
  
for k in range(1, 200):
  print(k)

#Here 3 is used to show the increment . 
# As 1 , 1+3 = 4 , 4+3 = 7 ..Till 12 
for k in range(1, 12, 3):
  print(k)