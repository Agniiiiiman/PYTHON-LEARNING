n = int(input("ENTER THE SERIES: "))
a = []  

for i in range(n):
    word = input("ENTER A WORD: ")
    a.append(word)

for word in a:
    if word[0] == word[-1]:  
        print("The word with same 1st and last letter is:", word)