def load_inventory():
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


# Load existing orders
orders = load_inventory()


# Display current orders
print("Current Orders:")
print()

for order in orders:
    print(f"{order[0]}, {order[1]}, {order[2]}")