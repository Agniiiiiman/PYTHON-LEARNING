"""
Change Item Value
To change the value of a specific item, refer to the index number:
replacing the value acoording to the the index number
"""
a = ["apple", "banana", "cherry"]
a[1] = "blackcurrant"
print(a)

#Change the second value by replacing it with two new values:

b = ["apple", "banana", "cherry"]
b[1:2] = ["blackcurrant", "watermelon"]
print(b)

#Change the second and third value by replacing it with one value:

c = ["apple", "banana", "cherry"]
c[1:3] = ["watermelon"]
print(c)

"""
Remove Specified Item
The remove() method removes the specified item.

ExampleGet your own Python Server
Remove "banana":
"""

d= ["apple", "banana", "cherry"]
d.remove("banana")
print(d)
"""
If there are more than one item with the specified value, the remove() method removes the first occurrence:

Example
Remove the first occurrence of "banana":
"""

e = ["apple", "banana", "cherry", "banana", "kiwi"]
e.remove("banana")
print(e)
"""
Remove Specified Index
The pop() method removes the specified index.

Example
Remove the second item:
"""

f = ["apple", "banana", "cherry"]
f.pop(1)
print(f)
"""
If you do not specify the index, the pop() method removes the last item.

Example
Remove the last item:
"""
g = ["apple", "banana", "cherry"]
g.pop()
print(g)
"""
The del keyword also removes the specified index:

Example
Remove the first item:
"""

h= ["apple", "banana", "cherry"]
del h[0]
print(h)
"""
The del keyword can also delete the list completely.

Example
Delete the entire list:
"""

i= ["apple", "banana", "cherry"]
del i
"""
Clear the List
The clear() method empties the list.

The list still remains, but it has no content.

Example
Clear the list content:
"""

j = ["apple", "banana", "cherry"]
j.clear()
print(j)
