import copy

l = []
n = int(input("Enter number of sublists for nested list: "))

for i in range(n):
    sublist = list(map(int, input(f"Enter elements of sublist {i+1} separated by spaces: ").split()))
    l.append(sublist)

# Create copies AFTER the list is completed
shallow_copy = copy.copy(l)
deep_copy = copy.deepcopy(l)

print("Original list:", l)
print("Shallow copy :", shallow_copy)
print("Deep copy    :", deep_copy)

