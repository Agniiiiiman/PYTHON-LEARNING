def max(arr):
    max = arr[0]
    for num in arr[1:]:
        if num > max:
            max = num
    return max

def min(arr):
    min=arr[0]
    for num in arr[1:]:
        if num > min:
            min=num
    return min        



n = int(input("Enter number of elements: "))
arr = []

print("Enter", n, "elements:")
for _  in range(n):
    arr.append(int(input()))

print("Maximum =", max(arr))
print("Minimum =", min(arr))
