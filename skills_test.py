# PYTHON SKILLS EXERCISE
# James Merrill
# 2/24/2017

x = 4 #ASSIGN AN INTEGER TO A VARIABLE
y = 3.14 #ASSIGN A FLOAT TO A VARIABLE

#USE SIMPLE MATH OPERATORS:
print x + y 
print x - y 
print x * y 
print x / y

#+= FOR ADDING AND CHANGING VARIABLE
z = 5
z += 2
print z

#% FOR DIVIDING AND RETURNING REMAINDER
a = 10
b = 4
print a % b

#LOGICAL OPERATORS and, or, not
p, q, r = 10, 20, 30
print p > q and q < r
print p < q and q < r
print p > q or q < r

print not p == 10 #not makes True = False

#ELIF STATEMENT
j = 9
if j == 10:
    print 'j = 10'
elif j == 9:
    print 'j = 9'
else:
    print 'j doesnt equal 9 or 10'

#FOR LOOP
for counter in range(0,10):
    print counter

#FOR LOOP w/ TUPLE
colors = ('red', 'green', 'blue', 'yellow')

print("The colors are:")
for color in colors:
    print color
