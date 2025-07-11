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
