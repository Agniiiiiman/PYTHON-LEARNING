n = int(input("Enter size of array: "))
arr = []
ue=set()
de=[]

for i in range(1,n+1):
    a=int(input("Enter Number"))
    arr.append(a)
for i in arr:
    if i not in ue:
        de.append(i)
        ue.add(i)
for j in ue:
    print(j)
