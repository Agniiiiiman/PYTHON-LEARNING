def num_to_word(n: int) -> str:
    ones = ["zero", "one", "two", "three", "four", "five", "six",
            "seven", "eight", "nine", "ten", "eleven", "twelve",
            "thirteen", "fourteen", "fifteen", "sixteen",
            "seventeen", "eighteen", "nineteen"]

    tens = ["", "", "twenty", "thirty", "forty", "fifty",
            "sixty", "seventy", "eighty", "ninety"]

    if n < 20:
        return ones[n]
    elif n < 100:
        return tens[n // 10] + ("" if n % 10 == 0 else " " + ones[n % 10])
    else:
        return ones[n // 100] + " hundred" + ("" if n % 100 == 0 else " and " + num_to_word(n % 100))

# Main program
if __name__ == "__main__":
    num = int(input("Enter a number (0-999): "))
    if 0 <= num <= 999:
        print("In words:", num_to_word(num))
    else:
        print("Number out of range!")
