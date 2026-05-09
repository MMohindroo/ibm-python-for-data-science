# THIS IS A COMMENT
"""
this is a multi line comment until i assign it to a variable 
"""

# Creating Variables
a = 5 # a is a int
b = 'Manan' # b is a str
print(a)
print(b)

# Casting 
# If i want to specifiy a variable's data type

c = str(55)
d = int (55)
e = float(55)
print(c, d, e)

# Get the data type 
# by using type ()
f = 69
g = "mac"
h = 6.9
print (type(f))
print (type(g))
print (type(h))

# we can use both single and double quotes for string 
apple = "Mango"
banana ='banana'
print (apple, banana)

# CASE SENSITIVE
A = "Apple"
a = 654654
# ARE 2 DIFFERENT VARIABLES
print(A,a)

# Many values to multiple Variables
i, j, k = "orange", 646, 'hen'
print (i, j, k)

# One value to multiple variables

l = m = n = "Dry Fruits"
print(l, m, n)

# Unpack a Collection (list or tuple)

fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)