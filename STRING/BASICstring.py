"""
Strings
Strings in python are surrounded by either single quotation marks, or double quotation marks.

'hello' is the same as "hello".

"""
# Quotes Inside Quotes
print("It's alright")
print("He is called 'Johnny'")
print('He is called "Johnny"')

# Assigning a string to a variable is done with the variable name followed by an equal sign and the string:
a = "Hello"
print(a)

#Multiline Strings=You can assign a multiline string to a variable by using three quotes:
a = """gacher pata sobuj
gacher pata subuj 
kan tanle matha ase """
print(a)

#Strings are Arrays - Square brackets can be used to access elements of the string.

a = "Hello, World!"
print(a[1]) # return will be 'e'

#Since strings are arrays, we can loop through the characters in a string, with a for loop.

for x in "banana":
  print(x)

#To get the length of a string, use the len() function.
a = "Hello, World!"
print(len(a))

#Check String -To check if a certain phrase or character is present in a string, we can use the keyword "in".
txt = "The best things in life are free!"
print("free" in txt)

# using it in an if statement :Print only if "free" is present:
txt = "The best things in life are free!"
if "free" in txt:
  print("Yes, 'free' is present.")

#Check if NOT
#To check if a certain phrase or character is NOT present in a string, we can use the keyword not in.
txt = "The best things in life are free!"
print("expensive" not in txt)

#Use it in an if statement:print only if "expensive" is NOT present:
txt = "The best things in life are free!"
if "expensive" not in txt:
  print("No, 'expensive' is NOT present.")