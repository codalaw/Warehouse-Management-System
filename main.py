import functions as inventory


while True:
    inventory.main_menu()

    choice = input("\nSelect an option (1-5): ").strip()

    if choice == "1":
        inventory.add_product()

    elif choice == "2":
        inventory.view_inventory()

    elif choice == "3":
        inventory.search_product()

    elif choice == "4":
        inventory.update_stock()

    elif choice == "5":
        print("\nThank you for using the Warehouse Management System!")
        print("Goodbye!")
        break

    else:
        print("\nInvalid option. Please select a number from 1 to 5.")
        input("\nPress Enter to try again...")