# shopping list
shopping_list = ["milk", "bread", "eggs", "butter", "juice", 
                 "sugar", "salt", "biscuits", "tea", "coffee"]

# 1. Display all items using a loop
print("Your current shopping list:")
for item in shopping_list:
    print("-", item)

# 2. Ask the user if they want to add a new item
add_item = input("\nDo you want to add a new item? (yes/no): ").strip().lower()

if add_item == "yes":
    new_item = input("Enter the item to add: ").strip().lower()
    shopping_list.append(new_item)
    print(f"'{new_item}' has been added to the shopping list.")

# 3. Ask the user if they want to remove any item
remove_item = input("\nDo you want to remove an item? (yes/no): ").strip().lower()

if remove_item == "yes":
    item_to_remove = input("Enter the item to remove: ").strip().lower()
    if item_to_remove in shopping_list:
        shopping_list.remove(item_to_remove)
        print(f"'{item_to_remove}' has been removed from the list.")
    else:
        print("Item not found.")

# 4. Display the updated list
print("\nUpdated shopping list:")
for item in shopping_list:
    print("-", item)
