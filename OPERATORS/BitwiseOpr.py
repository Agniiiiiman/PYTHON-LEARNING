"""
& =	AND	Sets each bit to 1 if both bits are 1	x & y	
|=	OR	Sets each bit to 1 if one of two bits is 1	x | y	
^=	XOR	Sets each bit to 1 if only one of two bits is 1	x ^ y	
~ =	NOT	Inverts all the bits	~x	
<< =	Zero fill left shift	Shift left by pushing zeros in from the right and let the leftmost bits fall off	x << 2	
>>	=Signed right shift	Shift right by pushing copies of the leftmost bit in from the left, and let the rightmost bits fall off	x >> 2
"""
# Define two numbers
a = 10      # binary: 1010
b = 4       # binary: 0100

print("a =", a, "->", bin(a))
print("b =", b, "->", bin(b))

# AND
and_result = a & b
print("\nAND (a & b):", and_result, "->", bin(and_result))

# OR
or_result = a | b
print("OR (a | b):", or_result, "->", bin(or_result))

# NOT
not_a = ~a
print("NOT (~a):", not_a, "->", bin(not_a))

# XOR
xor_result = a ^ b
print("XOR (a ^ b):", xor_result, "->", bin(xor_result))

# Zero fill left shift
left_shift = a << 2
print("Zero Fill Left Shift (a << 2):", left_shift, "->", bin(left_shift))

# Signed right shift
right_shift = a >> 2
print("Signed Right Shift (a >> 2):", right_shift, "->", bin(right_shift))

#The bin() function in Python is used to convert an integer to its binary representation as a string.