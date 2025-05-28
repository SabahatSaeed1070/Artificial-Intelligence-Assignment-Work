# Create a list
fruits = ["apple", "banana", "cherry", "date"]

# Access items in a list
print("First item:", fruits[0])          # Output: apple
print("Last item:", fruits[-1])          # Output: date

# Use loop with list
print("\nLoop through list:")
for fruit in fruits:
    print(fruit)

# Add items to a list
fruits.append("elderberry")              # Add to end
fruits.insert(2, "blueberry")            # Insert at position 2
print("\nAfter adding items:", fruits)

# Remove items from a list
fruits.remove("banana")                  # Removes 'banana'
popped_item = fruits.pop(1)              # Removes item at index 1
print("After removal:", fruits)
print("Popped item:", popped_item)

# Sort a list
fruits.sort()
print("Sorted list:", fruits)

# Copy a list
fruits_copy = fruits.copy()
print("Copied list:", fruits_copy)

# List comprehension
# Create a list of square numbers from 1 to 5
squares = [x**2 for x in range(1, 6)]
print("Squares using list comprehension:", squares)
