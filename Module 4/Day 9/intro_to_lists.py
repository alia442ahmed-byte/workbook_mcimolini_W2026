groceries = ["letuce", "tomato", "bread", "milk", "cheese", "apples"]

print("Grocery list: ")
print(groceries)

# Access an item at an index (0 based index)
print("The 3rd item on our grocery list is: ")
print(groceries[2])
print("The 1st item on our grocery list is: ")
print(groceries[0])

# Modifying list items
groceries[0] = "romaine lettuce" # changes our first item

print("The 1st item on our grocery list is: ")
print(groceries[0])
print("Grocery list: ")
print(groceries)

# Slicing lists - not a permanent change unless you reassign the output to the variable
print("The first 3 items are: ")
print(groceries[0:3]) # 0 could be left out

print("The last 2 items: ")
print(groceries[-2:])
# len() gets the length of my list
print(groceries[len(groceries) - 2:]) # the same as above, I can use variables as my index

item_input = input(f"What item would you like? (0 - {len(groceries) - 1}) ") # len(groceries) - 1 will give us the highest index we can choose before we get an IndexError
item_index = int(item_input)
print(f"You have selected {groceries[item_index]}")