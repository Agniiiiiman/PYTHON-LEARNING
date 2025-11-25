import math

def poly_perimeter(n: int, s: int) -> float:
    return round(n * s, 2)

def poly_area(n: int, s: int) -> float:
    return round((n * s * s) / (4 * math.tan(math.pi / n)), 2)

# Main
n = int(input("Enter number of sides (>=3): "))
s = int(input("Enter side length (>0): "))

if n >= 3 and s > 0:
    print("Perimeter:", poly_perimeter(n, s))
    print("Area:", poly_area(n, s))
else:
    print("Invalid input!")
