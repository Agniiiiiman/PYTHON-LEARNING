import copy

# 1. Create a list of numbers and sort them in descending order
numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))
numbers.sort(reverse=True)
print("Sorted in descending order:", numbers)

# 2. Remove all duplicate elements from a list using count() and remove()
nums = list(map(int, input("Enter numbers with duplicates separated by spaces: ").split()))
for num in nums[:]:
    while nums.count(num) > 1:
        nums.remove(num)
print("List after removing duplicates:", nums)

# 3. Make a shallow copy and deep copy of a nested list and test the difference
nested_list = []
n = int(input("Enter number of sublists for nested list: "))
for i in range(n):
    sublist = list(map(int, input(f"Enter elements of sublist {i+1} separated by spaces: ").split()))
    nested_list.append(sublist)

shallow_copy = copy.copy(nested_list)
deep_copy = copy.deepcopy(nested_list)

# Modify original
nested_list[0][0] = int(input("Enter a number to modify the first element of first sublist: "))

print("Original list:", nested_list)
print("Shallow copy:", shallow_copy)
print("Deep copy:", deep_copy)

# 4. Combine two lists using extend(). Then reverse the final list.
list1 = list(map(int, input("Enter elements of first list: ").split()))
list2 = list(map(int, input("Enter elements of second list: ").split()))
list1.extend(list2)
list1.reverse()
print("Combined and reversed list:", list1)

# 5. Create a list of names and find how many times a name appears.
names = input("Enter names separated by spaces: ").split()
name_to_check = input("Enter the name to check: ")
count = names.count(name_to_check)
print(f"'{name_to_check}' appears {count} times in the list.")
