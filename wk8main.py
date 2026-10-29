import json
from wk8product import Product
from wk8inventory import Inventory

def load_inventory():
    inventory = Inventory()

    try:
        with open("inventory.json", "r") as file:
            products = json.load(file)

        for item in products:
            product = Product(
                item["id"],
                item["name"],
                item["price"],
                item["stock"]
            )
            inventory.add_product(product)

    except FileNotFoundError:
        print("Inventory file not found. Starting with empty inventory.")

    return inventory

def save_inventory(inventory):
    products = []

    for product in inventory.get_products():
        product_data = {
            "id": product.product_id,
            "name": product.name,
            "price": product.price,
            "stock": product.stock
        }

        products.append(product_data)

    with open("inventory.json", "w") as file:
        json.dump(products, file, indent=4)

    print("Inventory saved successfully.")


def display_menu():
    print("\n========== INVENTORY MENU ==========")
    print("1. Display All Products")
    print("2. Add Product")
    print("3. Update Stock")
    print("4. Search Product")
    print("5. Save Inventory")
    print("6. Exit")
    print("====================================")


def add_product(inventory):
    print("\n--- Add New Product ---")

    while True:
        product_id = input("Enter Product ID: ").strip()

        if inventory.search_product(product_id) is not None:
            print("This product ID already exists. Please try again.")
        elif product_id == "":
            print("Product ID cannot be empty. Please try again.")
        else:
            break

    name = input("Enter Product Name: ").strip()

    if name == "":
        print("Product name cannot be empty.")
        return

    while True:
        try:
            price = float(input("Enter Price: $"))

            if price < 0:
                print("Price cannot be negative.")
            else:
                break

        except ValueError:
            print("Invalid price. Please enter a number.")

    while True:
        try:
            stock = int(input("Enter Stock Quantity: "))

            if stock < 0:
                print("Stock cannot be negative.")
            else:
                break

        except ValueError:
            print("Invalid stock. Please enter a whole number.")

    product = Product(product_id, name, price, stock)
    inventory.add_product(product)

    print("Product added successfully!")


def update_stock(inventory):
    print("\n--- Update Stock ---")

    product_id = input("Enter Product ID: ")
    product = inventory.search_product(product_id)

    if product is None:
        print("Product not found.")
        return

    print(f"Product: {product.name}")
    print(f"Current Stock: {product.stock}")

    try:
        new_stock = int(input("Enter New Stock Quantity: "))

        if new_stock < 0:
            print("Stock cannot be negative.")
            return

    except ValueError:
        print("Invalid input. Please enter a whole number.")
        return

    product.update_stock(new_stock)
    print("Stock updated successfully!")


def search_product(inventory):
    print("\n--- Search Product ---")

    product_id = input("Enter Product ID: ")
    product = inventory.search_product(product_id)

    if product is not None:
        print("\nProduct Found:")
        product.display_information()
    else:
        print("Product not found.")


def main():
    print("Welcome to the Inventory Management System!")

    inventory = load_inventory()

    while True:
        display_menu()
        option = input("Enter your choice: ")

        if option == "1":
            inventory.display_all()

        elif option == "2":
            add_product(inventory)

        elif option == "3":
            update_stock(inventory)

        elif option == "4":
            search_product(inventory)

        elif option == "5":
            save_inventory(inventory)

        elif option == "6":
            save_inventory(inventory)
            print("Thank you for using the Inventory Management System!")
            break

        else:
            print("Invalid option. Please enter a number from 1 to 6.")


if __name__ == "__main__":
    main()
