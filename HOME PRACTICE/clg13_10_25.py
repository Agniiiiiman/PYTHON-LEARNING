import random
import math

# 1. Generate a random float between 0 and 1
print("\n1. Random float between 0 and 1:", random.random())

# 2. Generate a random integer between given limits
low = int(input("\nEnter lower limit (for random integer): "))
high = int(input("Enter upper limit: "))
print("2. Random integer between", low, "and", high, ":", random.randint(low, high))

# 3. Randomly select an item from a list of strings
items = input("\nEnter some strings separated by commas: ").split(",")
print("3. Randomly selected item:", random.choice(items))

# 4. Shuffle a list of integers randomly
nums = list(map(int, input("\nEnter integers separated by spaces: ").split()))
random.shuffle(nums)
print("4. Shuffled list:", nums)

# 5. Generate a random number from a range with step size
start = int(input("\nEnter start of range: "))
stop = int(input("Enter end of range: "))
step = int(input("Enter step size: "))
print("5. Random number from range:", random.randrange(start, stop + 1, step))

# 6. Pick a random character from a string
string = input("\nEnter a string: ")
print("6. Random character:", random.choice(string)) 

# 7. Create a list of N random integers between 1 and 100
n = int(input("\nHow many random integers do you want (1–100)? "))
random_list = [random.randint(1, 100) for _ in range(n)]
print("7. Random integers list:", random_list)

# 8. Simulate rolling two six-sided dice and return the sum
dice_sum = random.randint(1, 6) + random.randint(1, 6)
print("\n8. Sum of two dice rolls:", dice_sum)

# 9. Set a seed and generate a predictable sequence
seed_val = int(input("\nEnter a seed value: "))
random.seed(seed_val) 
predictable_nums = [random.randint(1, 100) for _ in range(5)]
print("9. Predictable sequence:", predictable_nums)

# 10. Select 5 unique random numbers from a given range
end = int(input("\nEnter range end (for 1–end): "))
unique_nums = random.sample(range(1, end + 1), 5)
print("10. 5 unique random numbers:", unique_nums)

# 11. Simulate a lottery draw: pick 6 unique numbers from 1 to 49
lottery = random.sample(range(1, 50), 6)
print("\n11. Lottery numbers:", lottery)

# 12. Function to return n random elements from a given list
def pick_random_elements(lst, n):
    return random.sample(lst, n)

lst = input("\nEnter a list of items separated by commas: ").split(",")
k = int(input("How many items to pick randomly? "))
print("12. Randomly picked elements:", pick_random_elements(lst, k))

# 13. Compare randint() and randrange()
print("\n13. randint(1,10):", random.randint(1, 10))
print("13. randrange(1,11):", random.randrange(1, 11))

# 14. Generate a random float between two given numbers
a = float(input("\nEnter first number: "))
b = float(input("Enter second number: "))
print("14. Random float between", a, "and", b, ":", random.uniform(a, b))
 