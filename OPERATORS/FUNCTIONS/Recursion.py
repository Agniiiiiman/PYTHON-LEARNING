#FACTORIAL OF A NUMBER 

def factorial(n):
    if n==0:
        return 1
    else:
        return n*factorial(n-1)

print("FACTORIAL OF A NUMBER 5 IS:",factorial(5))
# OUTPUT 120



#Fibonacci Series (Nth Term)

def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

print("6th Fibonacci number:", fibonacci(6))
