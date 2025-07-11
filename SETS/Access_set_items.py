# DEFINATION Access Items
"""
You cannot access items in a set by referring to an index or a key.

But you can loop through the set items using a for loop, or ask if a specified value is present in a set, by using the in keyword.


Loop through the set, and print the values:
"""
a= {"apple", "banana", "cherry"}

for x in thisset:
  print(x)
"""
Check if "banana" is present in the set:
"""

b = {"apple", "banana", "cherry"}

print("banana" in b)
"""
Example
Check if "banana" is NOT present in the set:
"""

c = {"apple", "banana", "cherry"}

print("banana" not in c)

#Change Items=Once a set is created, you cannot change its items, but you can add new items.