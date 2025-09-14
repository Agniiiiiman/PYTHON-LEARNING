import math

# Function to calculate perimeter
def poly_perimeter(n: int, s: int) -> float:
    return round(n * s, 2)

# Function to calculate area
def poly_area(n: int, s: int) -> float:
    return round((n * (s ** 2)) / (4 * math.tan(math.pi / n)), 2)

# Main program
if __name__ == "__main__":
    n = int(input("Enter the number of sides (>=3): "))
    s = int(input("Enter the length of each side: "))

    if n < 3 or s <= 0:
        print("Invalid input. Number of sides must be >=3 and side length >0.")
    else:
        perimeter = poly_perimeter(n, s)
        area = poly_area(n, s)

        print(f"Perimeter of polygon: {perimeter}")
        print(f"Area of polygon: {area}")
