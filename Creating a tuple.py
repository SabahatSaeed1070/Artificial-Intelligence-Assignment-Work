# Creating a tuple
my_tuple = ("apple", "banana", "cherry")

# Accessing tuple items
print("First item:", my_tuple[0])
print("Last item:", my_tuple[-1])

# Looping through a tuple
print("\nLoop through tuple:")
for item in my_tuple:
    print(item)

# Joining tuples
tuple1 = (1, 2, 3)
tuple2 = (4, 5)
joined_tuple = tuple1 + tuple2
print("\nJoined tuple:", joined_tuple)

# Updating a tuple (indirectly by converting to a list and back)
temp_list = list(my_tuple)
temp_list[1] = "blueberry"
updated_tuple = tuple(temp_list)
print("Updated tuple:", updated_tuple)

# Unpacking a tuple
person = ("Alice", 25, "Engineer")
name, age, profession = person
print("\nUnpacked tuple:")
print("Name:", name)
print("Age:", age)
print("Profession:", profession)

# Tuple methods
numbers = (5, 1, 3, 5, 2, 5)
print("\nCount of 5:", numbers.count(5))     # How many times 5 appears
print("Index of 3:", numbers.index(3))       # First index of 3
