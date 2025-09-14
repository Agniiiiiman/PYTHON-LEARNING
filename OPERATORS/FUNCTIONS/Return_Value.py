#multiple of 5
def my_function(x):
  return 5 * x

print(my_function(3))
print(my_function(5))
print(my_function(9))

#Square of a Number
def square(n):
    return n * n

print(square(4))
print(square(10))


# Convert Celsius to Fahrenheit
def to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

print(to_fahrenheit(0))    # Output: 32.0
print(to_fahrenheit(37))   # Output: 98.6

#Area of Circle
def area_circle(radius):
    return 3.1416 * radius * radius

print(area_circle(5))
print(area_circle(10))

#Check Even or Odd
def is_even(num):
    return num % 2 == 0

print(is_even(4))  # True
print(is_even(7))  # False
