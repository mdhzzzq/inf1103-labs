def load_inventory():
    orders = []

    try:
        with open("inventory.txt", "r") as file:
            for line in file:
                line = line.strip()

                if line:
                    parts = line.split(",")

                    order_id = int(parts[0].strip())
                    product_name = parts[1].strip()
                    quantity = int(parts[2].strip())

                    orders.append([order_id, product_name, quantity])

    except FileNotFoundError:
        return []

    return orders


def save_inventory(orders):
    with open("inventory.txt", "w") as file:
        for order in orders:
            file.write(f"{order[0]}, {order[1]}, {order[2]}\n")


# Load existing orders
orders = load_inventory()


# Display current orders
print("Current Orders:")
print()

for order in orders:
    print(f"{order[0]}, {order[1]}, {order[2]}")

print()


# Get new order information
product_name = input("Enter Product Name: ")
quantity = int(input("Enter Quantity: "))


# Generate new order ID
if orders:
    new_order_id = orders[-1][0] + 1
else:
    new_order_id = 1001


# Create new order
new_order = [new_order_id, product_name, quantity]


# Add new order to history
orders.append(new_order)


# Display new order
print()
print("New Order Added:")
print(f"{new_order[0]}, {new_order[1]}, {new_order[2]}")
print()


# Save orders to file
save_inventory(orders)

print("Order successfully saved to inventory.txt")