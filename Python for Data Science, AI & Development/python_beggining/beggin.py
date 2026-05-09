a = 5
b = 6.5
c = "Hello! World"

type(a)
type(b)
type(c)

# integers are whole numbers, floats are decimal numbers, and strings are sequences of charactors. 
# type is a build-in function that returns the type of an object
# integers are finite numbers from negative to positive numbers 
# floats are decimal numbers and can also be both positive and negative numbers 
# But the difference is floats or decimal numbers can be a subset of integers
# Meaning we can write 2 (an integer) as 2.0 (a float) but we cannot do the opposite

# We can convert strings into integers or floats if the string is a number
# We can also convert integer into floats and strings
# We can also convert floats into integers and strings

# converting string to integer

x = 100
y = str(x)
type(x)
type(y)
print(y)

alpha = 'Minimize the damage control'
print(len(alpha))
for sey in alpha:
    print(sey)