# Original tuple of students' marks
marks = (78, 85, 90, 67, 72)

# I. Print the first and last elements of the tuple
print("First mark:", marks[0])
print("Last mark:", marks[-1])

# II. Unpack the tuple elements into separate variables
m1, m2, m3, m4, m5 = marks
print("\nUnpacked marks:")
print("m1 =", m1)
print("m2 =", m2)
print("m3 =", m3)
print("m4 =", m4)
print("m5 =", m5)

# III. Create a new tuple by adding 5 marks to each element
updated_marks = tuple(mark + 5 for mark in marks)

# IV. Print both the original and the new tuples
print("\nOriginal marks tuple:", marks)
print("Updated marks tuple (+5):", updated_marks)
