n = int(input("Enter a number: "))

if n >= 0:
    rev = int(str(n)[::-1])
else:
    rev = -int(str(-n)[::-1])

print("Reversed number:", rev)
