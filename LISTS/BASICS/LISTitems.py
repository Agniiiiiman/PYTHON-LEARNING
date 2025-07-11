# LIST ITEMS
"""
List items are ordered, changeable, and allow duplicate values.

List items are indexed, the first item has index [0], the second item has index [1] etc.

"""
# ODERED LIST

ordered_list = []

# Function to add item in order
def add_item(item):
    ordered_list.append(item)
    ordered_list.sort()  # Keeps the list sorted

# Function to remove item
def remove_item(item):
    if item in ordered_list:
        ordered_list.remove(item)
    else:
        print("Item not found.")

# Function to search item
def search_item(item):
    return item in ordered_list

# Function to display list
def show_list():
    print("Ordered List:", ordered_list)


# Example usage
add_item(10)
add_item(5)
add_item(8)
add_item(2)

show_list()                # [2, 5, 8, 10]

print("Is 8 in list?", search_item(8))     # True
print("Is 100 in list?", search_item(100)) # False

remove_item(5)
show_list()                # [2, 8, 10]
