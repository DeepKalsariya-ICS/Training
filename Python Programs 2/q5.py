# Create a python program to manage shopping list.
# Take input from user
# This process must not stop unless user enters nothing
# Use functions/methods to manage each operation
# Manage validations such as if the item not found
# On 8th option display list in tabular format
# 	Inputs :
# 		1 Add an item
# 		2 Add multiple items
# 		3 Add an item at index
# 		4 Remove last added item
# 		5 Remove an item with name
# 		6 Remove all items/ Empty list
# 		7 Replace an item with new item
# 		8 Display list


from prettytable import PrettyTable

def add_item(shopping_list):
    item = input("Enter item to add: ")
    if item:
        shopping_list.append(item)
        print(f"'{item}' added to the shopping list.")
    else:
        print("No item entered.")

def add_multiple_items(shopping_list):
    items = input("Enter items to add: ")
    if items:
        items_list = [item.strip() for item in items.split()]
        shopping_list.extend(items_list)
        print(f"Items {items_list} added to the shopping list.")
    else:
        print("No items entered.")

def add_item_at_index(shopping_list):
    try:
        index = int(input("Enter index: "))
        item = input("Enter item to add: ")
        if item:
            shopping_list.insert(index, item)
            print(f"'{item}' added at index {index}.")
        else:
            print("No item entered.")
    except ValueError:
        print("Invalid index. Please enter a valid number.")
    except IndexError:
        print("Index out of range.")

def remove_last_item(shopping_list):
    if shopping_list:
        item = shopping_list.pop()
        print(f"'{item}' removed from the shopping list.")
    else:
        print("Shopping list is already empty.")

def remove_item_by_name(shopping_list):
    item = input("Enter the name of the item to remove: ")
    if item in shopping_list:
        shopping_list.remove(item)
        print(f"'{item}' removed from the shopping list.")
    else:
        print(f"'{item}' not found in the shopping list.")

def empty_list(shopping_list):
    shopping_list.clear()
    print("Shopping list has been emptied.")

def replace_item(shopping_list):
    old_item = input("Enter the item to replace: ")
    if old_item in shopping_list:
        new_item = input("Enter the new item: ")
        index = shopping_list.index(old_item)
        shopping_list[index] = new_item
        print(f"'{old_item}' replaced with '{new_item}'.")
    else:
        print(f"'{old_item}' not found in the shopping list.")

def display_list(shopping_list):
    if shopping_list:
        table = PrettyTable()
        table.field_names = ["Index", "Item"]
        for index, item in enumerate(shopping_list):
            table.add_row([index, item])
        print("\nShopping List:")
        print(table)
    else:
        print("Shopping list is empty.")

def shopping_list():
    shopping_list = []
    options = {
        1: add_item,
        2: add_multiple_items,
        3: add_item_at_index,
        4: remove_last_item,
        5: remove_item_by_name,
        6: empty_list,
        7: replace_item,
        8: display_list
    }

    while True:
        print("\nOptions:")
        print("1. Add an item")
        print("2. Add multiple items")
        print("3. Add an item at index")
        print("4. Remove last added item")
        print("5. Remove an item with name")
        print("6. Remove all items / Empty list")
        print("7. Replace an item with a new item")
        print("8. Display list")
        print("0. Exit")

        choice = int(input("Enter your choice: "))
        if choice == 0:
            print("Program exited!")
            break
        elif choice in options:
            options[choice](shopping_list)
        else:
            print("Invalid choice.")


shopping_list()
