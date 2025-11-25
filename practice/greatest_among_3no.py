num1=int(input("ENTER 1ST NUMBER "))
num2=int(input("ENTER 2ND NUMBER "))
num3=int(input("ENTER 3RD NUMBER "))

if num1>num2 and num1>num3 :
    print("THE GREATEST NUMBER IS ",num1)

elif num2>num1 and num2>num3 :
    print("THE GREATEST NUMBER IS ",num2)

else:
    print("THE GREATEST NUMBER IS ",num3)