print("-------WELCOME TO MY SIMPLE CALCULATOR------")
print("CHOOSE OPTION ")
print("1.ADDITION ")
print("2.SUBTRACTION")
print("3.MULTIPLICATION ")
print("4.DIVISION")

choose=int(input("ENTER YOUR CHOICE :"))



num1=float(input("ENTER FIRST NUMBER: "))
num2=float(input("ENTER SECOND NUMBER:"))

if choose==1:
    sum=num1+num2
    print("ADDITION RESULT IS: ",sum)

elif choose==2:
    subs=num1-num2
    print("SUBTRACTION RESULT IS:",subs)


elif choose==3:
    mul=num1*num2
    print("MULTIPLICATION RESULT IS:",mul)

elif choose==4:
    if num1>num2:
        div=num1/num2
        print("DIVISION RESULT IS:",div)
    else:
        div=num2/num1
        print("DIVISION RESULT IS:",div)
else:
    print("WRONG CHOICE ")        



