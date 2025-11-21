# Take multiple strings as input, separated by spaces
strings = input("Enter strings separated by space: ").split()


f = sorted(strings, key=len)

print(f)
