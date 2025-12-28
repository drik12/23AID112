shopping_list = []
add_item = input("Enter an item to add to your shopping list: ")
while add_item.lower() != 'done':
    shopping_list.append(add_item)
    add_item = input("Enter another item to add (or type 'done' to finish): ")
remove_item = input("Enter an item to remove from your shopping list: ")
while remove_item.lower() != 'done':
    if remove_item in shopping_list:
        shopping_list.remove(remove_item)
    else:
        print(f"{remove_item} is not in the shopping list.")
    remove_item = input("Enter another item to remove (or type 'done' to finish): ")
show_list = print("Your current shopping list:", shopping_list)
quit = input("Type 'quit' to exit the program: ")
while quit.lower() != 'quit':
    quit = input("Type 'quit' to exit the program: ")