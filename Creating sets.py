# Creating sets
set1 = {1, 2, 3}
set2 = {3, 4, 5}

# add() - Add a single element
set1.add(6)
print("After add:", set1)

# update() - Add multiple elements (from list or set)
set1.update([7, 8])
print("After update:", set1)

# remove() - Remove an element (raises error if not found)
set1.remove(8)
print("After remove:", set1)

# discard() - Remove an element (does not raise error if not found)
set1.discard(10)  # No error if 10 not in set
print("After discard:", set1)

# pop() - Removes and returns a random element
popped = set1.pop()
print("Popped element:", popped)
print("After pop:", set1)

# clear() - Removes all elements
copy_set = set1.copy()
copy_set.clear()
print("After clear:", copy_set)

# union() - Combines two sets (all unique elements)
union_set = set1.union(set2)
print("Union:", union_set)

# intersection() - Common elements
intersection_set = set1.intersection(set2)
print("Intersection:", intersection_set)

# difference() - Elements in set1 but not in set2
difference_set = set1.difference(set2)
print("Difference:", difference_set)

# symmetric_difference() - Elements in either set, but not both
sym_diff = set1.symmetric_difference(set2)
print("Symmetric Difference:", sym_diff)

# issubset(), issuperset(), isdisjoint()
small_set = {1, 2}
big_set = {1, 2, 3, 4}
print("Is subset:", small_set.issubset(big_set))      # True
print("Is superset:", big_set.issuperset(small_set))  # True
print("Is disjoint:", set1.isdisjoint(set2))          # False
