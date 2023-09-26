# Initialize an empty shopping list
shopping_list = []

# Function to add items to the shopping list
def add_item():
    item = input("Enter the item to add: ")
    shopping_list.append(item)
    print(f"{item} has been added to your shopping list.")

# Function to delete items from the shopping list
def delete_item():
    item = input("Enter the item to delete: ")
    if item in shopping_list:
        shopping_list.remove(item)
        print(f"{item} has been removed from your shopping list.")
    else:
        print(f"{item} is not in your shopping list.")

# Function to display the current shopping list
def display_list():
    if shopping_list:
        print("Your current shopping list:")
        for item in shopping_list:
            print(item)
    else:
        print("Your shopping list is empty.")

# Main menu loop
while True:
    print("\nMenu:")
    print("1. Add item to shopping list")
    print("2. Delete item from shopping list")
    print("3. Display shopping list")
    print("4. Quit")
    
    choice = input("Enter your choice (1/2/3/4): ")
    
    if choice == '1':
        add_item()
    elif choice == '2':
        delete_item()
    elif choice == '3':
        display_list()
    elif choice == '4':
        print("Thank you for using the supermarket system. Goodbye!")
        break
    else:
        print("Invalid choice. Please select a valid option (1/2/3/4).") 