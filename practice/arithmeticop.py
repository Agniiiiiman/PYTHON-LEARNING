num1=int(input("Enter first number:"))
num2=int(input("Enter second number:"))
add=num1+num2
if num1 > num2:
    subs=num1-num2
    div=num1/num2

else:
    subs=num2-num1
    div=num2/num1

mul=num1*num2

print("ADDITION =" ,add)
print("Subtraction= ", subs )
print("MULTIPLICATION = ",mul)
print("DIVISION= ",div)
