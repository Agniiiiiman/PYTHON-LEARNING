#The else keyword in a for loop specifies a block of code to be executed when the loop is finished:
for x in range (6):
    print(x)
else:
    print("FINALLY FINISHED! ")


for x in range (6):
    if x==3: break
    print (x)
else:
    print("THIS IS THE END!!")
    