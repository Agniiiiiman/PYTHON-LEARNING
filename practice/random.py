my_dict = {'a': 1, 'b': '', 'c': None, 'd': 'hello', 'e': []}

cleaned = {k: v for k, v in my_dict.items() if v}
print(cleaned)
# Output: {'a': 1, 'd': 'hello'}
