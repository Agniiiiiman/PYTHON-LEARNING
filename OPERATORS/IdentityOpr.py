"""
is =	Returns True if both variables are the same object	x is y	
is not=	Returns True if both variables are not the same object	x is not y
"""
x = ["apple", "banana"]
y = ["apple", "banana"]
z = x

print(x is z)

# returns True because z is the same object as x

print(x is y)

# returns False because x is not the same object as y, even if they have the same content

print(x == y)

# to demonstrate the difference betweeen "is" and "==": this comparison returns True because x is equal to y

a = ["apple", "banana"]
b = ["apple", "banana"]
c = a

print(a is not c)

# returns False because z is the same object as x

print(a is not b)

# returns True because x is not the same object as y, even if they have the same content

print(a != b)

# to demonstrate the difference betweeen "is not" and "!=": this comparison returns False because x is equal to y