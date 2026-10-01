def load_orders():
    orders = []

    try:
        with open("orders.txt", "r") as file:
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


def save_orders(orders):
    with open("orders.txt", "w") as file:
        for order in orders:
            file.write(f"{order[0]}, {order[1]}, {order[2]}\n")


def get_product_name():
    return input("Enter Product Name: ")


def get_quantity():
    return int(input("Enter Quantity: "))


# Load existing orders
orders = load_orders()

# Display current orders
print("Current Orders:")
print()

for order in orders:
    print(f"{order[0]}, {order[1]}, {order[2]}")

print()

# Get new order information
product_name = get_product_name()
quantity = get_quantity()

# Generate new order ID
if orders:
    new_order_id = orders[-1][0] + 1
else:
    new_order_id = 1001

# Create and add new order
new_order = [new_order_id, product_name, quantity]
orders.append(new_order)

# Display new order
print()
print("New Order Added:")
print(f"{new_order[0]}, {new_order[1]}, {new_order[2]}")
print()

# Save orders
save_orders(orders)

print("Order successfully saved to orders.txt")