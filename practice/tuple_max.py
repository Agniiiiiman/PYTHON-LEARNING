n = int(input("Enter number of elements: "))
nums = tuple(int(input(f"Enter number {i+1}: ")) for i in range(n))

print("TUPLE:", nums)
print("MAXIMUM:", max(nums))
print("MINIMUM:", min(nums))
