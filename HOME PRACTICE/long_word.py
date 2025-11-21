words = input("Enter words: ").split()

index = int(input("Enter index: "))

if 0 <= index < len(words):
    sw = words[index]
    print("Word at index", index, "is:", sw)

    
    long = max(words, key=len)

    if sw == long:
        print("This is the longest word among the input.")
    else:
        print("This is not the longest word. The longest word is:", long)
else:
    print("ERROR")


