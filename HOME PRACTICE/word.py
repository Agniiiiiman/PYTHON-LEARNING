# wap to find word with same start and end letter 
s = input("Enter a string elememt  : ")
words = s.split()

sl = [word for word in words if word[0].lower() == word[-1].lower()]

print ("SAME LETTER ",sl)