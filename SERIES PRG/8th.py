a=int(input("ENTER FIRST TERM (A):"))
r=int(input("ENTER COMMON RATIO(R):"))
n=int(input("ENTER NUMBER OF TERMS :"))

for i in range(n):
    print(a*(r**i),end=" ")