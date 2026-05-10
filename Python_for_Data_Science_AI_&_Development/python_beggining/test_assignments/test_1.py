# Section 1
# Output & comments
# 1
# Print the text Hello, Python! exactly as shown.

# 2
# Print three lines in a single print() call using \n:
# Line 1, Line 2, Line 3

# 3
# Write a single-line comment saying what the program does, then a multi-line comment explaining two things it will print.

# Answer 1

print("Hello, Python!")

# Answer 2

print('God of war')
print('God of war')
print('God of war')
 
# Answer 3

x = 55
y = 100

print (x * y)
# This program is writen in a way that it is going to provide the product of x and y
'''
and the product of x and y is 5500
'''

# Section 2
# Variables & data types
# 4
# Create one variable of each type: str, int, float, bool. Print each variable and its type using type().

# 5
# Assign values to three variables in a single line (multiple assignment). Print all three.

# 6
# Create a variable x = 10. Reassign it to a string "ten". Print x and its type both times to show that Python variables can change type.

# Answer 4
e = "huiiii"
q = 50
w = 5.0
print(type(e))
print(type(q))
print(type(w))

# Answer 5

fruits = {"apple", "banana", "orange"}
"""I dont remember next"""

# Answer 6

x =10
print(type(x))
x = "ten"
print = (type(x))

# Section 3

# Task 7: Create an int variable and a float variable. Print both along with their types using type().
# Task 8: Create a variable storing a very large integer (e.g. a billion). Create another storing a negative float. Print both.
# Task 9: Create a complex number using Python's built-in complex number support (e.g. 3+5j). Print it and its type.

# Answer 7

u = 7
print(u)
print (type(u))

i = 7.7
print (i)
print (type(i))

# Answer 8

p = 879879878979878978979879789789789789465435476841324684735416874534631546816875546546546546545464545
a = -7.754648

print (p)

print (a)

# Answer 9

f = 3+5j
print (f)
print(type(f))

# Section 4
# Casting (type conversion)
# 10
# You have age = "19" (a string). Cast it to an integer, add 1 to it, and print the result.

# 11
# Convert 3.99 to an int and print the result. Then convert 7 to a float. What do you notice about the decimal conversion?

# Add a comment in your code explaining what you noticed.

# 12
# Convert the integer 0 and the integer 100 to bool. Print both results. Then convert the string "Hello" and an empty string "" to bool. Print both.

# Answer 10
age = "19"
print(int(age) + 1)

# Answer 11

k = 3.99
print(int(k))
l = 7
print(float(l))
'''
what i observe is that when i convert a float into int, it doesn't changes to nearst number but it converts into the number before decimal
and when i convert int into float then it just add a decimal and after that zero which doesn't change the actual value since 1 = 1.0
'''

# Answer 12
# i dont understand the question

# Section 5
# Putting it all together
# 13
# Create variables first_name, last_name, and age. Print a formatted sentence using an f-string:
# My name is Ravi Kumar and I am 20 years old.

# 14
# A shopkeeper has items = "50" (string) and price_per_item = 12.5 (float). Cast and calculate the total cost. Print:
# Total cost: 625.0

# 15
# Without running the code first, predict the output of each line below. Write your predictions as comments, then run and check:

# print(type(True))
# print(int(True) + int(False))
# print(float("3") + int("2"))
# print(bool("") == bool(0))

#Answer 12
first_name = 'Ravi'
last_name = 'Kumar'
age = 20
print ("My name is ", first_name, last_name ,' and I am ',age,' years old.')

#Answer 14
items = "50"
price_per_item = 12.5
Total_cost = int(items)*price_per_item
print(Total_cost)

#Answer 15 
# i haven't mention bool in screen shoot