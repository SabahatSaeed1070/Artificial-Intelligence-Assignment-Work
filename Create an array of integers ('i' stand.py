# Create an array of integers ('i' stands for integer)
import array

# Create an array of integers ('i' stands for integer)
arr = array.array('i', [10, 20, 30, 40])

# Accessing items
print("First element:", arr[0])

# Appending an item
arr.append(50)
print("After append:", arr)

# Inserting an item at index 1
arr.insert(1, 15)
print("After insert:", arr)

# Removing an item
arr.remove(30)
print("After remove:", arr)

# Popping last item
arr.pop()
print("After pop:", arr)

# Loop through array
print("Loop through array:")
for item in arr:
    print(item)

# Find index of a value
print("Index of 20:", arr.index(20))
