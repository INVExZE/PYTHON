tuple = (1, 5 , 6)
print(type(tuple), tuple)

res = tuple.index(1) 
res = tuple.count(5) 
# res = tuple.count(5, 0, 3) 

tup = (1, 2 , "Sanjay")
print(tup)
print(len(tup))

print(tup[0])
print(tup[1])
print(tup[2])

# This will give error as in TUPLE are IMUTABLE.
'''tuple[0] = 90 
print(tuple)'''


# Tuple ( start : end : jumpIndex )
tup1 = tuple[0:3]
print(tup1)

# OPERATION ON TUPLES 

# res = tuple.index(0) 
# res = tuple.count(5) 
# res = tuple.count(5, 0, 2) 
