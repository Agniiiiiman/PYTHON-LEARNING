"""
Information can be passed into functions as arguments.

Arguments are specified after the function name, inside the parentheses. You can add as many arguments as you want, just separate them with a comma.

The following example has a function with one argument (fname). When the function is called, we pass along a first name, which is used inside the function to print the full name:
"""
def greet(name):
  print("Hello, " + name + "!")

greet("Agniv")
greet("Ananya")
greet("Raj")


def square(num):
  print("Square is:", num * num)

square(4)
square(9)
square(2)



def full_name(first, last):
  print(first + " " + last)

full_name("Agniv", "Bhattacharjee")
full_name("Elon", "Musk")


def rectangle(l, b):
  return l * b

area = rectangle(15, 12)
print("Area of rectangle is:", area)
