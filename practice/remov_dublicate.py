nums = list(map(int, input("ENTER NUMBERS WITH DUPLICATE SEPARATED BY SPACE: ").split()))

for num in nums[:]:       # iterate over a copy of the list
    while nums.count(num) > 1:
        nums.remove(num)  # remove duplicates of that number

print("LIST AFTER REMOVING DUPLICATES:", nums)
