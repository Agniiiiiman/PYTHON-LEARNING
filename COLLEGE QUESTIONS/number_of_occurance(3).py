# Count the number of occurrences of a given element in a list.
n = input("Enter the list of elements separated by commas: ")

l = [int(x) for x in n.split(",")]
e = int(input("Element to count: "))

c = l.count(e)

print(f"The element {e} appears {c} times in the list.")
