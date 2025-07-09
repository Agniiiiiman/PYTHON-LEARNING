# Program to print Fibonacci series using for loop

# Get the number of terms from the user
n = int(input("Enter the number of terms: "))

# First two terms
a, b = 0, 1

if n <= 0:
    print("Please enter a positive integer.")
elif n == 1:
    print("Fibonacci sequence up to 1 term:")
    print(a)
else:
    print("Fibonacci sequence:")
    for i in range(n):
        print(a, end=" ")
        a, b = b, a + b
