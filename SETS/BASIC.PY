"""
Set
Sets are used to store multiple items in a single variable.

Set is one of 4 built-in data types in Python used to store collections of data, the other 3 are List, Tuple, and Dictionary, all with different qualities and usage.

A set is a collection which is unordered, unchangeable*, and unindexed.

* Note: Set items are unchangeable, but you can remove items and add new items.

Sets are written with curly brackets.


Create a Set:
"""
a= {"apple", "banana", "cherry"}
print(a)

#Note: Sets are unordered, so you cannot be sure in which order the items will appear.
"""
Set Items
Set items are unordered, unchangeable, and do not allow duplicate values.

Unordered
Unordered means that the items in a set do not have a defined order.

Set items can appear in a different order every time you use them, and cannot be referred to by index or key.

Unchangeable
Set items are unchangeable, meaning that we cannot change the items after the set has been created.

Once a set is created, you cannot change its items, but you can remove items and add new items.

Duplicates Not Allowed
Sets cannot have two items with the same value.

Example
Duplicate values will be ignored:
"""

b = {"apple", "banana", "cherry", "apple"}

print(b)
#Note: The values True and 1 are considered the same value in sets, and are treated as duplicates:
"""
Example
True and 1 is considered the same value:
"""

c = {"apple", "banana", "cherry", True, 1, 2}

print(c)

#Note: The values False and 0 are considered the same value in sets, and are treated as duplicates:
#False and 0 is considered the same value:

d = {"apple", "banana", "cherry", False, True, 0}

print(d)
