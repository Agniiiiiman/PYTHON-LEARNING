"""
If you do not know how many arguments that will be passed into your function, 
add a * before the parameter name in the function definition.
"""

#printing all the fruits

def fruits(*names):
  for name in names:
    print("Fruit:", name)

fruits("Apple", "Banana", "Mango", "Orange")

#Access a Specific Argument

def show_color(*colors):
  print("My favorite color is", colors[1])

show_color("Red", "Blue", "Green")

#Sum of All Numbers Passed
def total_sum(*numbers):
  print("Total is:", sum(numbers))

total_sum(10, 20, 30)
total_sum(5, 15)

#Multiplication of all numbers

def multiply_all(*numbers):
    result = 1
    for num in numbers:
        result *= num
    print("Total multiplication is:", result)

multiply_all(2, 3, 4)  # Output: 24
