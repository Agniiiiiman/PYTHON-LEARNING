# wap to accept 2 list from user and find common element 
n1 = list(map(int, input("ENTER ELEMENTS IN LIST 1 : ").split()))


n2 = list(map(int, input("ENTER ELEMENTS IN LIST 2 : ").split()))


c = list(set(n1) & set(n2))


if c:
    print("COMMON ELEMENTS:", c)
else:
    print("NO COMMON ELEMENTS FOUND")
