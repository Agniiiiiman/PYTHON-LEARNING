a=[]
n=int(input("ENTER THE SIZE : "))
for i in range (1,n+1):
    m=int(input("ENTER THE NUMBER"))
    a.append(m)
max=a[0]
min=a[0]
for i in a:
    if (i>max):
        max=i


for i in a:
    if(i<min):
        min=i

print("THE MAXIMUM IS ",max)
print("THE MINIMUM IS ",min)


