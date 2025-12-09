list1=list(map(int,input("Enter element of first list : ").split()))
list2=list(map(int,input("Enter element of second list :").split()))

list.extend(list2)
list.reverse()
print("COMBINED AND REVERSE LIST: ",list1)