import json


def page_header(title):
    print("\n" + "=" * 50)
    print(title.center(50))
    print("=" * 50)


def main_menu():
    page_header("WAREHOUSE MANAGEMENT SYSTEM")
    print("""
    [1] Add Product
    [2] View Inventory
    [3] Search Product
    [4] Update Stock
    [5] Exit
    """)
    print("=" * 50)


def add_product():
    page_header("ADD PRODUCT")
    print("\nThis feature is under construction.")
    input("\nPress Enter to return to the main menu...")


def view_inventory():
    page_header("CURRENT WAREHOUSE INVENTORY")

    inventory = load_inventory()

    if not inventory["products"]:
        print("\nNo products currently in inventory.")
    else:
        print()
        for product in inventory["products"]:
            print(f"Product ID : {product['id']}")
            print(f"Name       : {product['name']}")
            print(f"Quantity   : {product['quantity']}")
            print(f"Location   : {product['location']}")
            print("-" * 50)

    input("\nPress Enter to return to the main menu...")


def search_product():
    page_header("SEARCH PRODUCT")

    inventory = load_inventory()

    try:
        item_ID = int(input("\nEnter Product ID: "))
    except ValueError:
        print("\nPlease enter a valid numerical product ID.")
        input("\nPress Enter to return to the main menu...")
        return

    for product in inventory["products"]:
        if item_ID == product["id"]:
            print("\nProduct found!")
            print("-" * 50)
            print(f"Product ID : {product['id']}")
            print(f"Name       : {product['name']}")
            print(f"Quantity   : {product['quantity']}")
            print(f"Location   : {product['location']}")
            print("-" * 50)
            break
    else:
        print(f"\nNo product found with ID {item_ID}.")

    input("\nPress Enter to return to the main menu...")


def update_stock():
    page_header("UPDATE STOCK")
    print("\nThis feature is under construction.")
    input("\nPress Enter to return to the main menu...")


def load_inventory():
    with open("inventory.json", "r") as file:
        inventory = json.load(file)

    return inventory