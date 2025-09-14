#Print the first n cube numbers.Example: Input → 4, Output → 1 8 27 64
n=int(input("ENTER NUMBER OF SERIES "))

for i in range(1,n+1):
    print(i** 3,end=" ")