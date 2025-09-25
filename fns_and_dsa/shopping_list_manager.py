# shopping_list_manager.py

def display_menu():
    print("Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")


def add_item(shopping_list):
    item = input("Enter the item to add: ").strip()
    if item:
        shopping_list.append(item)
        print(f"✅ '{item}' has been added to your shopping list.")
    else:
        print("⚠️ Item name cannot be empty.")

def remove_item(shopping_list):
    item = input("Enter the item to remove: ").strip()
    if item in shopping_list:
        shopping_list.remove(item)
        print(f"🗑️ '{item}' has been removed from your shopping list.")
    else:
        print(f"⚠️ '{item}' was not found in your shopping list.")

def view_list(shopping_list):
    if shopping_list:
        print("\n🛒 Your Shopping List:")
        for idx, item in enumerate(shopping_list, start=1):
            print(f"{idx}. {item}")
    else:
        print("Your shopping list is currently empty.")

def main():
    shopping_list = []
    actions = {
        '1': add_item,
        '2': remove_item,
        '3': view_list
    }
    while True:
        display_menu()
        choice = input("Enter your choice: ").strip()
        if choice in actions:
            actions[choice](shopping_list)
        elif choice == '4':
            print("👋 Goodbye!")
            break
        else:
            print("❌ Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
