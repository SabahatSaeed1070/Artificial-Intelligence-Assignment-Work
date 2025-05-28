# List of numbers
numbers = [5, 12, 7, 18, 9, 24, 3, 16, 11]

# Counters for each category
div_by_3 = 0
even_not_3 = 0
odd_not_3 = 0

# Loop through each number and apply conditions
for num in numbers:
    if num % 3 == 0:
        print(f"{num} is divisible by 3")
        div_by_3 += 1
    elif num % 2 == 0:
        print(f"{num} is even but not divisible by 3")
        even_not_3 += 1
    else:
        print(f"{num} is odd and not divisible by 3")
        odd_not_3 += 1

# Final counts
print("\nSummary:")
print("Numbers divisible by 3:", div_by_3)
print("Even but not divisible by 3:", even_not_3)
print("Odd and not divisible by 3:", odd_not_3)
