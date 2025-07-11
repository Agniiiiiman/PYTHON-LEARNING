"""
Join Sets
There are several ways to join two or more sets in Python.

The union() and update() methods joins all items from both sets.

The intersection() method keeps ONLY the duplicates.

The difference() method keeps the items from the first set that are not in the other set(s).

The symmetric_difference() method keeps all items EXCEPT the duplicates.

Union
The union() method returns a new set with all items from both sets.


Join set1 and set2 into a new set:
"""


set1 = {"a", "b", "c"}
set2 = {1, 2, 3}

set3 = set1.union(set2)
print(set3)


"""
You can use the | operator instead of the union() method, and you will get the same result.

Example
Use | to join two sets:
"""

set4 = {"a", "b", "c"}
set5 = {1, 2, 3}

set6 = set4 | set5
print(set6)

""""
Join Multiple Sets
All the joining methods and operators can be used to join multiple sets.

When using a method, just add more sets in the parentheses, separated by commas:

Example
Join multiple sets with the union() method:
"""

st1 = {"a", "b", "c"}
st2 = {1, 2, 3}
st3 = {"John", "Elena"}
st4 = {"apple", "bananas", "cherry"}

myse = st1.union(st2, st3, st4)
print(myse)


"""
When using the | operator, separate the sets with more | operators:

Example
Use | to join two sets:
"""

se1 = {"a", "b", "c"}
se2 = {1, 2, 3}
se3 = {"John", "Elena"}
se4 = {"apple", "bananas", "cherry"}

myset = se1 | se2 | se3 |se4
print(myset)


"""
Join a Set and a Tuple
The union() method allows you to join a set with other data types, like lists or tuples.

The result will be a set.

Example
Join a set with a tuple:
"""

x = {"a", "b", "c"}
y = (1, 2, 3)

z = x.union(y)
print(z)


"""
Note: The  | operator only allows you to join sets with sets, and not with other data types like you can with the  union() method.

Update
The update() method inserts all items from one set into another.

The update() changes the original set, and does not return a new set.

The update() method inserts the items in set2 into set1:
"""

sett1 = {"a", "b" , "c"}
sett2 = {1, 2, 3}

sett1.update(sett2)
print(sett1)
