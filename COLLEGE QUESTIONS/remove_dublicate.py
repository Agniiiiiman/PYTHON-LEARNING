#Remove all duplicates from a list.

a = [1, 2, 5, 2, 3, 1, 5]
final = []

for i in a:
    if i not in final:
        final.append(i)


print (list(set(a)))